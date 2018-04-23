from .models import Project, Task, User, TaskRel
from .forms import UserForm, TaskRelation, TaskForm
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from requests import request
from django.shortcuts import redirect
from django.db.models import Sum
from django.contrib import messages
import json


class Home(TemplateView):
    """
    Displaying active projects and tasks on home page
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
            context = super(Home, self).get_context_data(**kwargs)
            context.update({
                'tasks': Task.objects.filter(status=2),
                'projects': Project.objects.filter(status=2),
            })
            return context


class MyTaskList(TemplateView):
    """
    Displaying task list on task list page
    """
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
            context = super(MyTaskList, self).get_context_data(**kwargs)
            context.update({
                'tasks': Task.objects.all(),
                'tasksrel': TaskRel.objects.all(),
            })
            return context


class MyProjectList(ListView):
    """
    Displaying project list on project list page
    """
    template_name = 'project_list.html'
    model = Project

    def get_queryset(self):
        return Project.objects.all()


class TaskCreate(CreateView):
    """
    Display form for creating new task
    """
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = '/mytasks/'


class TaskUpdate(UpdateView):
    """
    Display form for update task
    """
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = '/mytasks/'
    queryset = Task.objects.all()


class TaskDelete(DeleteView):
    """
    Display form for removing task
    """
    model = Task
    template_name = 'delete_task.html'
    success_url = '/mytasks/'


# class HR(ListView):
#     template_name ='create_user.html'
#     model = User


# def hr(request):
#     form = UserForm()
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return redirect('hr_all')
#         else:
#             form = UserForm()
#     return render(request, 'create_user.html', {'form': form})


def hr_all(request):
    users = User.objects.all()
    return render(request, 'hr_all.html', {'users': users})


def json_to_gantt():
    """
    Convert tasks data to json output
    """
    output = list()
    i = 0
    for each_task in Task.objects.all():
        task_info = list()
        task_info.append(str(Task.objects.get(id=each_task.id).id))
        task_info.append(Task.objects.get(id=each_task.id).name)
        js_start_date = (
            Task.objects.get(id=each_task.id).start_date.year,
            Task.objects.get(id=each_task.id).start_date.month,
            Task.objects.get(id=each_task.id).start_date.day
        )
        task_info.append(js_start_date)
        js_end_date = (
            Task.objects.get(id=each_task.id).end_date.year,
            Task.objects.get(id=each_task.id).end_date.month,
            Task.objects.get(id=each_task.id).end_date.day
        )
        task_info.append(js_end_date)
        task_info.append(Task.objects.get(id=each_task.id).duration.days)
        task_info.append(Task.objects.get(id=each_task.id).percent_complete)
        js_predecessors = list()
        if TaskRel.objects.filter(successor__id=each_task.id).exists():
            for item in TaskRel.objects.filter(successor__id=each_task.id):
                js_predecessors.append(str(item.predecessors_id))

            task_info.append(','.join(js_predecessors))
        else:
            task_info.append('')
        output.append(task_info)
        i += 1
    response = json.dumps(output)
    return response


class ProjectDashboard(TemplateView):
    """
    Display project dashboard
    """
    template_name = 'project_dashboard.html'

    def get_context_data(self, pk, **kwargs):
        context = super(ProjectDashboard, self).get_context_data(**kwargs)
        context.update({
            'tasks': Task.objects.filter(project_id=pk),
            'project': Project.objects.filter(pk=pk),
            'tasksrel': TaskRel.objects.all(),
            'output': json_to_gantt(),
        })
        return context


class BusinessPlan(TemplateView):
    template_name = 'business_plan.html'

    def get_context_data(self, pk, **kwargs):
        context = super(BusinessPlan, self).get_context_data(**kwargs)
        context.update({
            'tasks': Task.objects.filter(project_id=pk),
        })
        context['opt_price'] = Task.objects.all().aggregate(Sum('optimistic_price'))
        context['pess_price'] = Task.objects.all().aggregate(Sum('pessimistic_price'))
        context['real_price'] = Task.objects.all().aggregate(Sum('realistic_price'))
        return context


def new_relation(request, pk):
    """
    Display form for creation of new relation between tasks with validation
    """
    form = TaskRelation()
    error_message = ''
    if request.method == 'POST':
        if pk != request.POST['predecessors']:
            task, created = TaskRel.objects.get_or_create(successor_id=pk, predecessors_id=request.POST['predecessors'])
            if not created:
                error_message = ('Такая связь уже существует',)
            else:
                return redirect('/mytasks')
        else:
            error_message = ('Нельзя связывать задачу с самой собой', )
    return render(request, 'create_rel.html', {'form': form, 'messages': error_message})


def upd_relation(request, pk):
    """
    Display form for editing relation between tasks with validation
    """
    form = TaskRelation()
    rel = TaskRel.objects.get(pk=pk)
    error_message = ''
    if request.method == 'POST':
        if int(rel.successor_id) == int(request.POST['predecessors']):
            error_message = ('Нельзя связывать задачу с самой собой', )
        elif TaskRel.objects.filter(
                predecessors_id=request.POST['predecessors'], successor_id=rel.successor_id).exists():
            error_message = ('Такая связь уже существует', )
        else:
            rel.predecessors_id = request.POST['predecessors']
            rel.save()
            return redirect('/mytasks')
    form = TaskRelation(initial={'predecessors': rel.predecessors})
    return render(request, 'edit_rel.html', {'form': form, 'rel': pk, 'messages': error_message})


def del_relation(request, pk):
    """
    Display form for removing task
    """
    form = None
    rel = TaskRel.objects.get(pk=pk)
    if request.method == 'POST':
        rel.delete()
        return redirect('/mytasks')
    else:
        return render(request, 'delete_rel.html', {'form': form, 'rel': rel})


class UserCreate(CreateView):
    """
    Create new user
    """
    form_class = UserForm
    template_name ='create_user.html'
    success_url = '/hr_all/'


class UserUpdate(UpdateView):
    """
    Edit users info
    """
    form_class = UserForm
    template_name ='create_user.html'
    success_url = '/hr_all/'
    queryset = User.objects.all()


class UserDelete(DeleteView):
    """
    Display form for removing user
    """
    model = User
    template_name = 'delete_user.html'
    success_url = '/hr_all/'
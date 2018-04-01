from .models import Project, Task, User, TaskRel
from .forms import UserForm, NewTask
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from requests import request
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

from django.views.generic.detail import DetailView


# Create your views here.

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
    # model = Task
    # def get_queryset(self):
    #     return Task.objects.all(), TaskRel.objects.all()

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


class HR(ListView):
    template_name = 'hr.html'
    model = User


def hr(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('hr_all')
        else:
            form = UserForm()
    # projects = Project.objects.all()
    return render(request, 'hr.html', {'form':form})
    # return render(request, 'hr.html', {'projects':projects})


def hr_all(request):
    users = User.objects.all()
    return render(request, 'hr_all.html', {'users': users})

# class HrList(ListView):
#     template_name ='hr_all.html'
#     model=User
#
#     def get_queryset(self):
#         return User.objects.all()

      
class ProjectDashboard(TemplateView):
    """
    Display project dashboard
    """
    template_name = 'project_dashboard.html'
    # model = Project

    def get_context_data(self, pk, **kwargs):
        context = super(ProjectDashboard, self).get_context_data(**kwargs)
        context.update({
            'tasks': Task.objects.filter(project_id=pk),
            'project': Project.objects.filter(pk=pk),
            'tasksrel': TaskRel.objects.all(),
        })
        return context


# def TaskCreate(request):
#     form = NewTask()
#     if request.method == 'POST':
#         # if form.is_valid():
#         task = Task(
#             wbs_code=form.cleaned_data["wbs_code"],
#             task_type=form.cleaned_data["task_type"],
#             name=form.cleaned_data["name"],
#             description=form.cleaned_data["description"],
#             start_date=form.cleaned_data["start_date"],
#             duration=form.cleaned_data["duration"],
#             end_date=form.cleaned_data["end_date"],
#             responsible=form.cleaned_data["responsible"],
#             status=form.cleaned_data["status"],
#             project=form.cleaned_data["project"],
#         )
#         task.save()
#         messages.add_message(request, messages.SUCCESS, "Новая задача создана")
#         # predecessors = TaskRel(
#         #     predecessors=form.cleaned_data["predecessors"],
#         #     successor=task.id,
#         # )
#         # predecessors.save()
#         return redirect('my_tasks/')
#         # else:
#         #     form = NewTask()
#         #     messages.add_message(request, messages.ERROR, "Задача не создана")
#     return render(request, 'create_task.html', {'form': form})


def task_create(request):
    form = NewTask()
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = Task(
                wbs_code=form.cleaned_data["wbs_code"],
                task_type=form.cleaned_data["task_type"],
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                start_date=form.cleaned_data["start_date"],
                duration=form.cleaned_data["duration"],
                end_date=form.cleaned_data["end_date"],
                responsible=form.cleaned_data["responsible"],
                status=form.cleaned_data["status"],
                project=form.cleaned_data["project"],
            )
            task.save()
            # predecessors = TaskRel(
            #     predecessors=form.cleaned_data["predecessors"],
            #     successor=task.id,
            # )
            # predecessors.save()
            messages.add_message(request, messages.SUCCESS, "Новая задача создана")
            return redirect('my_tasks/')
    else:
        form = NewTask()
    return render(request, 'create_task.html', {'form': form})


def task_edit(request, pk):
    cur_task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = NewTask(request.POST, instance=cur_task)
        if form.is_valid():
            task = Task(
                wbs_code=form.cleaned_data["wbs_code"],
                task_type=form.cleaned_data["task_type"],
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                start_date=form.cleaned_data["start_date"],
                duration=form.cleaned_data["duration"],
                end_date=form.cleaned_data["end_date"],
                responsible=form.cleaned_data["responsible"],
                status=form.cleaned_data["status"],
                project=form.cleaned_data["project"],
            )
            task.save()
            messages.add_message(request, messages.SUCCESS, "Задача изменена")
            return redirect('my_tasks/')
        else:
            form = NewTask(instance=cur_task)
        return render(request, 'create_task.html', {'form': form})



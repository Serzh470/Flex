from .models import Project, Task, User
from .forms import UserForm, BudgetForm
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from requests import request
from django.shortcuts import redirect
from django.db.models import Sum

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


class MyTaskList(ListView):
    """
    Displaying task list on task list page
    """
    template_name = 'task_list.html'
    model = Task

    def get_queryset(self):
        return Task.objects.all()


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
    form=UserForm()
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('hr_all')
        else:
            form = BudgetForm()
    # projects = Project.objects.all()
    return render(request, 'business_plan.html', {'form':form})
    # return render(request, 'hr.html', {'projects':projects})

def hr_all(request):
    users = Task.objects.all()
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
    model = Project

    def get_context_data(self, pk, **kwargs):
        context = super(ProjectDashboard, self).get_context_data(**kwargs)
        context.update({
            'tasks': Task.objects.filter(project_id=pk),
            'project': Project.objects.filter(pk=pk)
        })
        return context


class BusinessPlan(TemplateView):
    template_name = 'business_plan.html'

    def get_context_data(self, pk, **kwargs):
        context = super(BusinessPlan, self).get_context_data(**kwargs)
        context.update({
            'tasks': Task.objects.filter(project_id=pk),
            # 'project': Project.objects.filter(pk=pk)
        })
        context['opt_price'] = Task.objects.all().aggregate(Sum('optimistic_price'))
        return context





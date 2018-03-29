from .models import Project, Task, User
from .forms import UserForm
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from requests import request

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
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.save()
    #         return redirect('hr_all')
    #     else:
    #         form = UserForm()

    return render(request, 'hr.html', {'project':Project.name})

def hr_all(request):
    users = User.objects.all()
    return render(request, 'hr_all.html', {'users': users})

# class HrList(ListView):
#     template_name ='hr_all.html'
#     model=User
#
#     def get_queryset(self):
#         return User.objects.all()
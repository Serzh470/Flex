from django.shortcuts import render
from .models import Project, Task
from django.shortcuts import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView


# Create your views here.


class Home(ListView):
    """
    Displaying active projects on home page
    """
    template_name = 'home.html'
    model = Project

    def get_queryset(self):
        return Project.objects.filter(status='Ongoing')


class MyTaskList(ListView):
    """
    Displaying task list on task list page
    """
    template_name = 'task_list.html'
    model = Task

    def get_queryset(self):
        return Task.objects.all()


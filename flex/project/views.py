from django.shortcuts import render
from .models import Project, Task
from django.shortcuts import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView


# Create your views here.


class Home(TemplateView):
    """
    Displaying home page
    """
    template_name = 'home.html'
    model = Project

    def get_queryset(self):
        return Project.objects.all()


# def home(request):
#     return render(request, 'index.html', {'project': Project.name})


class MyTaskList(ListView):
    """
    Displaying task list
    """
    template_name = 'task_list.html'
    model = Task

    def get_queryset(self):
        return Task.objects.all()


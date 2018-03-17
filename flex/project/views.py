from django.shortcuts import render
from .models import Project, Task
from django.shortcuts import HttpResponse
from django.views.generic.list import ListView


# Create your views here.


def home(request):
    return render(request, 'index.html', {'project': Project.name})


class MyTaskList(ListView):

    template_name = 'task_list.html'
    model = Task

    def get_queryset(self):
        return Task.objects.all()

from .models import Project, Task
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
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


class ProjectDashboard(DetailView):
    """
    Display project dashboard
    """
    template_name = 'project_dashboard.html'
    model = Project


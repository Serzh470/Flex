from django.shortcuts import render
from .models import Project
from django.shortcuts import HttpResponse

# Create your views here.


def home(request):

    return render(request, 'index.html', {'project': Project.name})

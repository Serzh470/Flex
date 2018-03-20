from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import Project, Task
from django.shortcuts import resolve_url


# class TaskCreate(CreateView):
#     """
#     Create new task object
#     """
#     model = Task
#     template_name = 'create_task.html'
#     # fields = '__all__'
#     fields = [
#         'wbs_code',
#         'name',
#         'description',
#         'start_date',
#         'duration',
#         'duration',
#         'end_date',
#         'predecessor',
#         'responsible',
#         'status',
#         'project',
#     ]
#
#     def get_success_url(self):
#         return resolve_url('/mytasks/', pk=self.object.pk)

class TaskForm(forms.ModelForm):
    """
    Create new task object
    """
    wbs_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'WBS'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    description = forms.Textarea()
    start_date = forms.DateField(widget=forms.DateField())
    duration = forms.DurationField(widget=forms.DurationField)
    end_date = forms.DateField(widget=forms.DateField())
    predecessor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Previous task'}))
    responsible = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Responsible'}))
    status = forms.CharField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status'}))
    project = forms.CharField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Project'}))


    class Meta:

        model = Task
        # template_name = 'create_task.html'
        # fields = '__all__'
        fields = [
            'wbs_code',
            'name',
            'description',
            'start_date',
            'duration',
            'duration',
            'end_date',
            'predecessor',
            'responsible',
            'status',
            'project',
        ]


class TaskCreate(CreateView):
    form_class = TaskForm
    template_name = 'create_task.html'
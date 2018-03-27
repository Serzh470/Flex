from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import Project, Task, STATUS


class TaskForm(forms.ModelForm):
    """
    Create new task object
    """
    wbs_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'WBS код'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Описание'}))
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Старт: 01.12.1900'}))
    duration = forms.DurationField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Продолжительность: '}))
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Финиш: 01.12.1900'}))
    predecessor = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Предыдущая задача:'}))
    responsible = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Исполнитель'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Статус'}),
                             choices=STATUS)
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(), required=False, widget=forms.Select(attrs={
            'class': 'form-control', 'placeholder': 'Входит в проект'}))

    class Meta:
        model = Task
        fields = [
            'wbs_code',
            'name',
            'description',
            'start_date',
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
    success_url = '/mytasks/'


class TaskUpdate(UpdateView):
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = '/mytasks/'
    queryset = Task.objects.all()


class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = '/mytasks/'

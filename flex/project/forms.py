from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import Project, Task, STATUS, User, TASK_TYPE


class TaskForm(forms.ModelForm):
    """
    Create new task object
    """
    wbs_code = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'WBS код'}
        )
    )
    task_type = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Задача или Веха'}
        ), choices=TASK_TYPE
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Название'}
        )
    )
    description = forms.CharField(
        required=False, widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Описание'}
        )
    )
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'datepicker form-control'}
        ), required=False
    )
    duration = forms.DurationField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Продолжительность'}
        ), required=False
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'datepicker form-control'}
        ), required=False
    )
    responsible = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Исполнитель'}
        )
    )
    status = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Статус'}
        ), choices=STATUS
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(), required=False, widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Входит в проект'}
        )
    )

    class Meta:
        model = Task
        fields = [
            'wbs_code',
            'task_type',
            'name',
            'description',
            'start_date',
            'duration',
            'end_date',
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


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'job',
            'phone',
            'email',
            'project_role',
            'occupation',
            'other',
            'project'
        ]


class UserCreate(CreateView):
    form_class = UserForm
    template_name = 'hr.html'
    success_url = '/'


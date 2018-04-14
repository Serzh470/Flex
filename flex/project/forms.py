from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import Project, Task, STATUS, User, TASK_TYPE
from django.forms.widgets import TextInput
from django.utils.dateparse import parse_duration
import datetime
from django.core.exceptions import ValidationError


class DurationInput(TextInput):
    """
    Custom input widget for duration field, convert seconds in days
    """
    def format_value(self, value):
        if 'д' in value:
            day_number = int(value.replace('д', ''))
            days = datetime.timedelta(days=day_number)
        else:
            duration = parse_duration(value)
            second_number = duration.seconds
            days = datetime.timedelta(days=second_number)
        return '{}д'.format(days.days)


class DurationDayFiled(forms.DurationField):
    """
    Custom input field for input in days
    """
    def to_python(self, value):
        if 'д' in value:
            value = value.replace('д', '')
        return super().to_python(value)


class TaskForm(forms.ModelForm):
    """
    Create new task object for with many settings for each field
    """
    wbs_code = forms.CharField(
        label='WBS код',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    task_type = forms.ChoiceField(
        choices=TASK_TYPE,
        label='Тип',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    name = forms.CharField(
        label='Название',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    description = forms.CharField(
        label='Описание',
        required=False, 
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 3}
        )
    )
    start_date = forms.DateField(
        label='Дата начала',
        widget=forms.DateInput(
            attrs={'class': 'datepicker form-control'}
        ), required=False
    )    
    duration = DurationDayFiled(
        widget=DurationInput(
          required=False, 
          label='Продолжительность',
          attrs={'class': 'form-control'}
        )
    )
    end_date = forms.DateField(
        label='Дата завершения',
        required=False,
        widget=forms.DateInput(
            attrs={'class': 'datepicker form-control'}
        )
    )
    responsible = forms.CharField(
        label='Исполнитель',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    status = forms.ChoiceField(
        choices=STATUS,
        label='Статус',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    project = forms.ModelChoiceField(
        label='Проект',
        queryset=Project.objects.all(), required=False, widget=forms.Select(
            attrs={'class': 'form-control'}
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


class TaskRelation(forms.ModelForm):
    """
    Create new
    """
    predecessors = forms.ModelChoiceField(
        queryset=Task.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}), label='Предыдущая задача')

    class Meta:
        model = Task
        fields = [
            'predecessors',
        ]


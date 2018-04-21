from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import Project, Task, STATUS, User, TASK_TYPE, ROLE



class TaskForm(forms.ModelForm):
    """
    Create new task object
    """
    wbs_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'WBS код'}))
    task_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Задача или Веха'}),
                             choices=TASK_TYPE)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Описание'}))
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Старт', 'type': 'date'}))
    duration = forms.DurationField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Продолжительность'}))
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Финиш', 'type': 'date'}))
    predecessor = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Предыдущая задача'}))
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
            'task_type',
            'name',
            'description',
            'start_date',
            'duration',
            'end_date',
            'predecessor',
            'responsible',
            'status',
            'project',
            'optimistic_price',
            'pessimistic_price',
            'realistic_price'
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
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    job = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Должность'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    project_role = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Задача или Веха'}),
                             choices=ROLE)
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Занятость'}))
    other = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Другое'}))
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(), required=False, widget=forms.Select(attrs={
            'class': 'form-control', 'placeholder': 'Входит в проект'}))

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






class BudgetForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =[
            'wbs_code',
            'name',
            'description',
            'responsible',
            'status',
            'optimistic_price',
            'pessimistic_price',
            'realistic_price',
        ]

class BudgetCalculate(CreateView):
    form_class = BudgetForm
    template_name = 'business_plan.html'
    success_url = ''

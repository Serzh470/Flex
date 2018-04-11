from django.db import models

# variables
STATUS = (
    (1, 'Не начато'),
    (2, 'В работе'),
    (3, 'Отстает'),
    (4, 'Выполнено'),
    (5, 'Приостановлено'))

ROLE = (
    (1, 'Участник'),
    (2, 'Менеджер'),
    (3, 'Стейкхолдер'),)

TASK_TYPE = (
    (1, 'Задача'),
    (2, 'Веха'))


# Models
class Project(models.Model):
    """
    Project model
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    duration = models.DurationField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    project_manager = models.CharField(max_length=255)
    status = models.SmallIntegerField(choices=STATUS)

    def __str__(self):
        # return 'Project: {} | Project Manager: {} | Status: {}'.format(self.name, self.project_manager, self.status)
        return self.name

    def __unicode__(self):
        return self.name


class Task(models.Model):
    """
    Task & milestone model
    """
    wbs_code = models.CharField(max_length=32, unique=True)
    task_type = models.SmallIntegerField(choices=TASK_TYPE, default=1)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    responsible = models.CharField(max_length=255)
    status = models.SmallIntegerField(choices=STATUS)
    project = models.ForeignKey(Project, on_delete='PROTECT', null=True, blank=True)

    def __str__(self):
        return 'Task: {} | Responsible: {} | Status: {}'.format(self.name, self.responsible, self.status)


class User(models.Model):
    """
    User model
    """
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    job = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    project_role = models.SmallIntegerField(choices=ROLE)
    occupation = models.CharField(max_length=250)
    other = models.CharField(max_length=250)
    project = models.ForeignKey(Project, on_delete='PROTECT', null=True, blank=True)

    def __str__(self):
        return 'User: {}{} | Project Role: {} | Occupation: {}'.format(self.name, self.surname, self.project_role, self.occupation)


class TaskRel(models.Model):
    """Relationships between models"""
    predecessors = models.ForeignKey(Task, on_delete='PROTECT', null=True, blank=True, unique=False)
    successor = models.ForeignKey(Task, on_delete='PROTECT', related_name='+', null=True, blank=True, unique=False)

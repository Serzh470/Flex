from django.db import models


STATUS = (
    (1, 'Не начато'),
    (2, 'В работе'),
    (3, 'Отстает'),
    (4, 'Выполнено'),
    (5, 'Приостановлено')
)


ROLE = ((1,'Участник'),
        (2, 'Менеджер'),
        (3, 'Стейкхолдер'),
)

TASK_TYPE = ((1, 'Задача'), (2, 'Веха'))


# Create your models here.


class Project(models.Model):
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
    wbs_code = models.CharField(max_length=32, unique=True)
    task_type = models.SmallIntegerField(choices=TASK_TYPE, default=1)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    duration = models.DurationField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    predecessor = models.IntegerField(null=True, blank=True)
    # successor = models.IntegerField(null=True, blank=True)
    responsible = models.CharField(max_length=255)
    status = models.SmallIntegerField(choices=STATUS)
    project = models.ForeignKey(Project, on_delete='PROTECT', null=True, blank=True)

    def __str__(self):
        return 'Task: {} | Responsible: {} | Status: {}'.format(self.name, self.responsible, self.status)


class User(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    job = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    project_role = models.SmallIntegerField(choices=ROLE)
    occupation = models.CharField(max_length=250)
    other = models.CharField(max_length=250)
    project = models.ForeignKey(Project, on_delete='PROTECT', null = True, blank = True)

    def __str__(self):
        return 'User: {}{} | Project Role: {} | Occupation: {}'.format(self.name, self.surname, self.project_role, self.occupation)


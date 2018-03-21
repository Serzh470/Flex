from django.db import models


STATUS = (
    (1, u'Не начато'),
    (2, u'В работе'),
    (3, u'Отстает'),
    (4, u'Выполнено'),
    (5, u'Приостановлено')
)

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

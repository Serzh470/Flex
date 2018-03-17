from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    project_manager = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return 'Project: {} | Project Manager: {} | Status: {}'.format(self.name, self.project_manager, self.status)


class Task(models.Model):
    wbs_code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    responsible = models.CharField(max_length=255)
    status = models.CharField(max_length=64)
    project = models.ForeignKey(Project, on_delete='PROTECT', null=True, blank=True)

    def __str__(self):
        return 'Task: {} | Responsible: {} | Status: {}'.format(self.name, self.responsible, self.status)

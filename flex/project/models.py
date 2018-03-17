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
    project = models.ForeignKey(Project, on_delete='PROTECT')

    def __str__(self):
        return 'Task: {} | Responsible: {} | Status: {}'.format(self.name, self.responsible, self.status)

class User(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    job = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    project_role = models.CharField(max_length=100)
    occupation = models.CharField(max_length=250)
    other = models.CharField(max_length=250)

    def __str__(self):
        return 'User: {}{} | Project Role: {} | Occupation: {}'.format(self.name, self.surname, self.project_role, self.occupation)



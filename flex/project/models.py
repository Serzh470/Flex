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


def tasks_update(task_id, **kwargs):
    """
    Function for updating dates in tasks, if one task is changed.
    """
    if TaskRel.objects.filter(predecessors__id=task_id).exists():
        for next_task in TaskRel.objects.filter(predecessors__id=task_id).select_related('successor'):
            task_to_upd = next_task.successor
            if TaskRel.objects.filter(successor__id=task_to_upd.id).count() == 1:
                new_end = Task.objects.get(id=task_id).end_date
                task_to_upd.start_date = new_end
                task_to_upd.end_date = task_to_upd.start_date + task_to_upd.duration
                task_to_upd.save()
                tasks_update(task_to_upd.id)  # call function again for the next tasks
            # if task_to_upd has more, than one predecessor, define the latest finish date
            else:
                end_dates = dict()
                previous_tasks = TaskRel.objects.filter(successor__id=task_to_upd.id).select_related('predecessors')
                for each_task in previous_tasks:
                    end_dates[each_task.predecessors_id] = Task.objects.get(id=each_task.predecessors_id).end_date
                max_end_date = max(end_dates)
                task_to_upd.start_date = end_dates[max_end_date]
                task_to_upd.end_date = task_to_upd.start_date + task_to_upd.duration
                task_to_upd.save()
                tasks_update(task_to_upd.id)  # call function again for the next tasks


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
    percent_complete = models.BigIntegerField(default=0)
    project = models.ForeignKey(Project, on_delete='PROTECT', null=True, blank=True)

    def __str__(self):
        return 'Task: {} | Responsible: {} | Status: {}'.format(self.name, self.responsible, self.status)

    def save(self, *args, **kwargs):
        """
        Redefine save method for model of Task, update dates in others successors
        """
        if not self.id:
            if self.start_date and self.duration:
                self.end_date = self.start_date + self.duration
            super(Task, self).save()
            tasks_update(self.id)
        else:
            new_start = self.start_date
            new_duration = self.duration
            task_id = self.id
            self.end_date = new_start + new_duration
            old_start = Task.objects.get(id=task_id).start_date
            old_duration = Task.objects.get(id=task_id).duration
            super(Task, self).save()
            if new_start != old_start or new_duration != old_duration:
                tasks_update(task_id)


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

    def save(self, *args, **kwargs):
        """
        Redefine save method for model of TaskRel, update dates, if new relation is created
        """
        task_id = self.predecessors_id
        super(TaskRel, self).save()
        return tasks_update(task_id)

    def delete(self, *args, **kwargs):
        """
        Redefine delete method for model of TaskRel, update dates, if new relation is deleted
        """
        if len(TaskRel.objects.filter(successor__id=self.successor_id)) > 1:
            current_task = self.successor
            super(TaskRel, self).delete()
            previous_tasks = TaskRel.objects.filter(successor__id=current_task.id)
            end_dates = dict()
            for each_task in previous_tasks:
                end_dates[each_task.predecessors_id] = Task.objects.get(id=each_task.predecessors_id).end_date
            task_w_max_end_date = int(max(end_dates))
            tasks_update(task_w_max_end_date)
        else:
            super(TaskRel, self).delete()

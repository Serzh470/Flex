from django.contrib import admin
from .models import Project, Task, User, TaskRel

# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(User)
admin.site.register(TaskRel)




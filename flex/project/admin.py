from django.contrib import admin
from .models import Project, Task, User

# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(User)



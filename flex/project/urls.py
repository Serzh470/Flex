from django.conf.urls import url
from . import views
from .views import Home, MyProjectList, MyTaskList
from .forms import TaskCreate

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^mytasks/$', MyTaskList.as_view(), name='tasks'),
    url(r'^myprojects/$', MyProjectList.as_view(), name='projects'),
    url(r'^addtask/$', TaskCreate.as_view(), name='add_task'),
]
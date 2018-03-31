from django.conf.urls import url
from .views import Home, MyProjectList, MyTaskList, hr, hr_all
from .forms import TaskCreate, TaskUpdate, TaskDelete



urlpatterns = [
    url(r'^hr/$', hr, name = 'hr'),
    url(r'^hr_all/$', hr_all, name='hr_all'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^mytasks/$', MyTaskList.as_view(), name='tasks'),
    url(r'^myprojects/$', MyProjectList.as_view(), name='projects'),
    url(r'^addtask/$', TaskCreate.as_view(), name='add_task'),
    url(r'^updtask/(?P<pk>\d+)/$', TaskUpdate.as_view(), name='upd_task'),
    url(r'^deltask/(?P<pk>\d+)/$', TaskDelete.as_view(), name='del_task'),
]

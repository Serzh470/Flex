from django.conf.urls import url
from . import views
from .views import Home, MyProjectList, MyTaskList
from .forms import TaskCreate, TaskUpdate

urlpatterns = [
    url(r'hr/', views.hr, name = 'hr'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^mytasks/$', MyTaskList.as_view(), name='tasks'),
    url(r'^myprojects/$', MyProjectList.as_view(), name='projects'),
    url(r'^addtask/$', TaskCreate.as_view(), name='add_task'),
    url(r'^updtask/(?P<pk>\d+)/$', TaskUpdate.as_view(), name='upd_task')
]

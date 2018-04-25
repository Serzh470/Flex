from django.conf.urls import url

from .views import Home, MyProjectList, MyTaskList, hr_all, ProjectDashboard, BusinessPlan, new_relation, upd_relation, del_relation
from .views import TaskCreate, TaskUpdate, TaskDelete, UserCreate, UserUpdate, UserDelete


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^adduser/$', UserCreate.as_view(), name='new_user'),
    url(r'^upduser/(?P<pk>\d+)/', UserUpdate.as_view(), name='upd_user'),
    url(r'^deluser/(?P<pk>\d+)$', UserDelete.as_view(), name='del_user'),
    url(r'^hr_all/$', hr_all, name='hr_all'),
    url(r'^mytasks/$', MyTaskList.as_view(), name='tasks'),
    url(r'^myprojects/$', MyProjectList.as_view(), name='projects'),
    url(r'^addtask/$', TaskCreate.as_view(), name='add_task'),
    url(r'^updtask/(?P<pk>\d+)/$', TaskUpdate.as_view(), name='upd_task'),
    url(r'^deltask/(?P<pk>\d+)/$', TaskDelete.as_view(), name='del_task'),
    url(r'^project_dashboard/(?P<pk>\d+)/$', ProjectDashboard.as_view(), name='project_dashboard'),
    url(r'^project_dashboard/(?P<pk>\d+)/budget/$', BusinessPlan.as_view(), name='business_plan'),
    url(r'^new_rel_task/(?P<pk>\d+)/$', new_relation, name='new_rel_task'),
    url(r'^upd_rel_task/(?P<pk>\d+)/$', upd_relation, name='upd_rel_task'),
    url(r'^del_rel_task/(?P<pk>\d+)/$', del_relation, name='del_rel_task')
]
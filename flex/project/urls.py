from django.conf.urls import url
from . import views
from .views import Home, MyProjectList, MyTaskList

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^mytasks/$', MyTaskList.as_view(), name='tasks'),
    url(r'^myprojects/$', MyProjectList.as_view(), name='projects'),
]
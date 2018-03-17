from django.conf.urls import url
from . import views
from .views import MyTaskList

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^mytasks/$', MyTaskList.as_view(), name='tasks'),
]
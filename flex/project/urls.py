from django.conf.urls import url
from . import views
from .views import MyTaskList, Home

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^mytasks/$', MyTaskList.as_view(), name='tasks'),
]
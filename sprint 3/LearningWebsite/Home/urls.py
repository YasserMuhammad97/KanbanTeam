from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$', views.index,name = 'Home'),
    url(r'^login/$', login, {'template_name' : 'Home/login.html'}),
    url(r'^register/$', views.register , name='register')]

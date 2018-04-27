from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^$', views.index,name = 'Home'),
    url(r'^login/$', login, {'template_name' : 'Home/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'Home/logout.html'}),
    url(r'^contactus/$' ,views.contacttus , name= 'contact us'),
    url(r'^instructors/$' , views.instructors , name = 'instructors'),
    url(r'^java/$', views.coursesjava, name = 'java'),
    url(r'^database/$', views.coursesdatabase, name='database'),
    url(r'^graphics/$', views.coursesgraphics, name='grahpics'),
    url(r'^aboutus/$' , views.aboutus, name = 'about us '),
    url(r'^register/$', views.register , name='register')]

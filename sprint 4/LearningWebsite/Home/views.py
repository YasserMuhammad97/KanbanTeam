from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from Home.forms import RegisterationForm
from Home.forms import contact_us
from django.views.generic import TemplateView

def contacttus(request):
        form = contact_us()
        return render(request, 'ContactUs/contact us .html' , {'form' : form})

def instructors(request):
    return render(request , 'Instructor/instructor.html')

def coursesjava(request):
    return render(request , 'Courses/java.html')

def coursesdatabase(request):
    return render(request , 'Courses/database.html')

def coursesgraphics(request):
    return render(request , 'Courses/graphics.html')

def index(request):
    form = RegisterationForm()

    args = {'form': form}
    return render(request,'Home/Home/index_home.html', args)

def contactus(request):

    return render(request, 'ContactUs/contact us .html')

def aboutus(request):
    return render(request , 'AboutMe/aboutme.html')

def register(request):
    if request.method=='POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form= RegisterationForm()

        args = {'form': form}
        return render(request, 'Home/signup.html', args)

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from Home.forms import RegisterationForm
def index(request):

    return render(request,'Home/Home/index_home.html')

def register(request):
    if request.method=='POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Home')
    else:
        form= RegisterationForm()

        args = {'form': form}
        return render(request, 'Home/signup.html', args)

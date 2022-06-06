from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
import requests
import json
import urllib

def categories(request):
    return render(request, 'LoginSystem/categories.html')

def IndividualStream(request, sport_id):
    return render(request, 'LoginSystem/individualstream.html')

def home(request):
    return render(request, 'LoginSystem/index.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form=CreateUserForm()
        if request.method == 'POST':
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.RECAPTCHA_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:               
                form=CreateUserForm(request.POST)
                if form.is_valid():
                    user=form.save()
                    fname=form.cleaned_data.get('first_name')
                    lname=form.cleaned_data.get('last_name')

                    Profile.objects.create(
                        user=user,
                    )
                    messages.success(request, 'Account was created for '+fname+' '+lname)
                    return redirect('login')
            else:
                messages.info(request, 'Invalid captcha ')

        context={'form': form}
        return render(request, 'LoginSystem/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.RECAPTCHA_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                user=authenticate( request, username=username, password=password)

                if user is not None:               
                    login(request, user)
                    return redirect('dashboard')        

                else:
                    messages.info(request, 'Username OR password is incorrect')
            else:
                messages.info(request, 'Invalid captcha ')
                
        context={}
        return render(request, 'LoginSystem/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboardPage(request):   
 return render(request, 'LoginSystem/dashboard.html')

def streams(request):
    return HttpResponse('streams')

def user(request):
    return HttpResponse('user')








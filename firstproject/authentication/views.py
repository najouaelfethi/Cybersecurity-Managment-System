from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserDNSSI



@login_required
def HomePage(request):
    return render(request, 'authentication/index.html', {})

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        # Verify that the username and email do not already exist
        if User.objects.filter(username=name).exists():
            return HttpResponse('Username already exists')
        if User.objects.filter(email=email).exists():
            return HttpResponse('Email already exists')

        # Create the new user
        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')
  
    return render(request, 'authentication/register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Error, user does not exist')

    return render(request, 'authentication/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('landing')

def test(request):
    return render(request, 'authentication/test.html', {})

def HomePage(request):
    return render(request, 'authentication/home.html', {})

def landinpage(request):
    return render(request, 'authentication/landinpage.html', {})

def login_DNSSI(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username and password are correct
        if UserDNSSI.objects.filter(username=username, password=password).exists():
            # Redirect to the DNSSI.html page
            return redirect('evaluation')
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'authentication/login_DNSSI.html', {'error_message': error_message})
    else:
        return render(request, 'authentication/login_DNSSI.html', {})
    
def dropmenu(request):   
    return render(request, 'dropmenu.html') 



from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages

def log_in(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Sucessfully!")	
            return redirect('homepage')
        else:
            messages.success(request, "There Was An Error Logging In, Try Again...")	
            return redirect('login')
    else:
		    return render(request, 'registration/login.html', {})
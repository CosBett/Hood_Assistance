from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from . forms import SignupForms

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
    

def signup(request):
    if request.method == 'POST':
        form = SignupForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form =  SignupForms     

    signup_context = {'form':form}
    
    return render(request, 'registration/signup.html', signup_context)

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out Sucessfully!")	

    return redirect('landingpage')


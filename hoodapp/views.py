from django.shortcuts import render,redirect
from . models import Profile,Hood,Post,Business
from .forms import HoodForm, BusinessForm,PostForm,UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def landing_page(request):
    pass
    return render(request,'landing_page.html', {}) 

@login_required 
def index(request):
    hoods = Hood.objects.all()
    hoods = hoods[:: -1]
    
    context ={
        'hoods':hoods
    }
    return render(request, 'index.html', context )

@login_required
def edit_profile(request, username):
    profile = Profile.objects.all()
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)

    edit_profile_context={'form': form ,'profile':profile}    
    return render(request, 'profile.html',edit_profile_context )

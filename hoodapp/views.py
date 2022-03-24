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

@login_required
def create_Business(request):
    businesses= Business.objects.all()
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = request.user
            business.save()
            return redirect('business')
    else:
        form = BusinessForm()
    business_context= {'form': form, 'businesses':businesses}    
    return render(request, 'Business.html',business_context)



def myhood(request, hood_id):
    hoods = Hood.objects.get(id=hood_id)
    businesses = Business.objects.filter(hood=hoods)
    posts = Post.objects.filter(hood=hoods)
    posts = posts[::-1]
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hoods
            post.user = request.user
            post.save()
            return redirect('myhood.html', hoods.id)
    else:
        form = PostForm()
    myhood_context = { 'hoods': hoods,'posts': posts,'form': form,'businesses':businesses
    }
    return render(request, 'single_hood.html', myhood_context)
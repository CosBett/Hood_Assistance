from django.shortcuts import render
from . models import Profile,Hood,Post,Business

def landing_page(request):
    pass
    return render(request,'landing_page.html', {}) 
def index(request):
    hoods = Hood.objects.all()
    hoods = hoods[:: -1]
    
    context ={
        'hoods':hoods
    }
    return render(request, 'index.html', {context} )
    
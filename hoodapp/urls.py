from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landingpage'),
    path('home/', views.index, name='homepage'),
    path('profile/<username>', views.edit_profile, name='profile'),
    path('business/', views.create_Business,name='business' )
    ]
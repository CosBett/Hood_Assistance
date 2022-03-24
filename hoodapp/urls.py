from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landingpage'),
    path('home/', views.index, name='homepage'),
    path('profile/<username>', views.edit_profile, name='profile'),
    path('business/', views.create_Business,name='business' ),
    path('myhood/<hood_id>', views.myhood, name='hood' ),
    path('<hood_id>/members', views.hood_members, name='members'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),

    ]
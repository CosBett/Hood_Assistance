from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Hood(models.Model):
    name = models.CharField(max_length=150, blank=False)
    location = models.CharField(max_length=100)
    occupants_Count = models.ImageField(upload_to='images/')
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='ad')
    description = models.TextField(max_length=500, blank=False)
    photo = models.ImageField(upload_to='images/')
    police_contact = models.ImageField(upload_to='images/')
    Health_contact = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}hood'
    
    def create_hood(self):
        self.save()

    def find_hood(cls,name):
        return cls.objects.filter(name__icontains=name).all()

    def save_hood(self):
        self.save()
        
    def delete_hood(self):
        self.delete()

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=150, blank=False)
    hood = models.ForeignKey(Hood, on_delete=models.SET_NULL, related_name='member', blank=True, null=True )

    def __str__(self):
        return f'{self.username}Profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    def save_profile(self):
        self.save()    

    def delete_profile(self):
        self.delete()
        
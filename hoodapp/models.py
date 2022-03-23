from django.db import models


class Hood(models.Model):
    name = models.CharField(max_length=150, blank=False)
    location = models.CharField(max_length=100)
    occupants_Count = models.ImageField(upload_to='images/')
    admin = models.ForeignKey("User", on_delete=models.CASCADE, related_name='ad')
    description = models.TextField(max_length=500, blank=False)
    photo = models.ImageField(upload_to='images/')
    police_contact = models.ImageField(upload_to='images/')
    Health_contact = models.IntegerField(null=True, blank=True)
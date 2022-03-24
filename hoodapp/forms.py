from django import forms
from .models import Profile, Hood, Post, Business

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'hood')



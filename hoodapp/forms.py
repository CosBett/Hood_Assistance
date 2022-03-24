from django import forms
from .models import Profile, Hood, Post, Business

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'hood')

class HoodForm(forms.ModelForm):
    class Meta:
        model =Hood
        exclude = ('admin',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'hood')
        
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text','image')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text','image')


class EditProfile(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'password',
            'first_name',
            'email',
            'last_name',
            
        }
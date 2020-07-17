from django import forms
from .models import Post, Comment, Userinfo
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable media-editor-textarea postcontent'})

        }


class CommentForm(forms.ModelForm):

    class Meta:

        model=Comment
        fields = ('author', 'text')

        Widgets = {

            'author' : forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable media-editor-textarea'})}

class Userform(forms.ModelForm):

    class Meta:

        model=User
        fields=('username', 'email', 'password')

class ProfileForm(forms.ModelForm):

    class Meta:
        model=Userinfo
        fields="__all__"

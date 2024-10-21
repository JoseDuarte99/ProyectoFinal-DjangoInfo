from django import forms

from apps import post
from .models import Category, Post, Comments
from django.views.generic.edit import UpdateView
from django.utils.translation import gettext_lazy as _


class CommentsForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Ingrese cometario'}),
        label=''
    )

    class Meta:
        model = Comments
        fields = ['text']


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'text', 'image', 'category')
        labels = {
            'title': _('Titulo'),
            'subtitle': _('Subtitulo'),
            'text': _('Texto'),
            'category': _('Categoria'),
            'image': _('Imagen'),
        }



class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'text', 'category', 'image']
        labels = {
            'title': _('Titulo'),
            'subtitle': _('Subtitulo'),
            'text': _('Texto'),
            'category': _('Categoria'),
            'image': _('Imagen'),
        }
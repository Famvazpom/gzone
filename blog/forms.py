# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from cProfile import label
from django import forms
from .models import *
from tinymce.widgets import TinyMCE
from django.core.files.images import get_image_dimensions
from PIL import Image
from io import BytesIO

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuario",
                "class": "form-control",
                "label": "Usuario",
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control",
                "label": "Contraseña",
            }
        ))

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class PerfilForm(forms.ModelForm):
    biografia = forms.CharField(widget=TinyMCE())
    class Meta:
        model= Perfil
        exclude = ['usuario']

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())
    descripcion = forms.Textarea()
    class Meta:
        model = Post
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(PostForm, self).__init__(*args, **kwargs)
       self.fields['autor'].queryset = Perfil.objects.filter(usuario=user)
       self.fields['autor'].initial = Perfil.objects.filter(usuario=user).first()

class PostUpdateForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())
    descripcion = forms.Textarea()
    class Meta:
        model = Post
        exclude= ['autor']
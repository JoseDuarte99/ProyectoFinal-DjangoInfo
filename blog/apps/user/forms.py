from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserChangeForm



#  --------------------------------------- REGISTRO ------------------------------------------------

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'image']
        labels = {
            'image': _('Foto de Perfil'),
        }



#  --------------------------------------- LOGUEO ------------------------------------------------

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)


#  --------------------------------------- USUARIOS ------------------------------------------------

class HiddenPasswordField(forms.CharField):          
    password_fake = forms.CharField(widget=forms.HiddenInput()) #Campo de contraseña falso

class UserAdministrationForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']

    password = HiddenPasswordField()  # Esto representará el campo de contraseña como una entrada oculta
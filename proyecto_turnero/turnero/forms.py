from django import forms
from .models import Cliente

from django.contrib.auth.forms import *

class ClienteRegisterForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=('nombre','cedula_ruc','prioridad','servicios')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput(), label='password')
    




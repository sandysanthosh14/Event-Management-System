from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Eventform(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'
class Eventlistform(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'

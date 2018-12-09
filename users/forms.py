from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = (
            'full_name', 'username', 'email', 'phone_number', 'cpf',
            'address', 'neighborhood', 'city', 'state', 'country',
            )

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ( 
            'full_name', 'username', 'email', 'phone_number', 'cpf',
            'address', 'neighborhood', 'city', 'state', 'country', 
            )
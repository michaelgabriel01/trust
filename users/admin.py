from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User

class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        'full_name', 'email', 'username', 'phone_number', 'cpf','address', 
        'neighborhood', 'city', 'state', 'country', 'creation_date',
    ]

admin.site.register(User, UserAdmin)
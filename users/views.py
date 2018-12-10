from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserCreationForm

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def our_service(request):
    return render(request, 'our-service.html')

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserCreationForm


# Register view
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# Our service view
def our_service(request):
    return render(request, 'our-service.html')

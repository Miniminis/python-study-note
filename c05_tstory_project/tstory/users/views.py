from django.shortcuts import render
from django.views.generic import FormView
from .forms import RegisterForm
from .models import User

# Create your views here.
class RegisterView(FormView):
    template_name = 'registration/register.html'
    success_url = '/accounts/login/'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()     
        return super().form_valid(form)



    
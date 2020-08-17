from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import RegisterForm, LoginForm
from .models import FcUser
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from .decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html', {'user' : request.session.get('user')})

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    return redirect('/')

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = FcUser(
            email=form.data.get('email'),
            pw=make_password(form.data.get('pw'))
        )
        user.save()

        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)

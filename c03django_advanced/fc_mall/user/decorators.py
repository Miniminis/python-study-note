from django.shortcuts import redirect
from .models import FcUser

def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        return function(request, *args, **kwargs)
    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        
        if user is None or not user:
            return redirect('/login')
        
        user_obj = FcUser.objects.get(email=user)
        if user_obj.level != 'admin':
            return redirect('/')
        
        return function(request, *args, **kwargs)
    
    return wrap






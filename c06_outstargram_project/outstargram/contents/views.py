from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

# 로그인 상태로만 접근 가능하기 때문에 자동으로 로그인 페이지로 redirect 처리
@method_decorator(login_required, name='dispatch')      
class HomeView(TemplateView):
    template_name = 'home.html'


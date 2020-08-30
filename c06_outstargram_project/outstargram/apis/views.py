from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.validators import validate_email, ValidationError

# Create your views here.
class BaseApiView(View):
    @staticmethod
    def response(data='{}', message='', status=200):
        result = {
            'data' : data,
            'message' : message
        }
        return JsonResponse(result, status)


class UserCreateView(BaseApiView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    
    def get(self, request):
        return self.response
    
    """ ajax 로 post 요청시, csrf_token 이 문제가 되는 경우가 있음. 
    이를 방지하기 위해, post method 처리시의 csrf token 에 대한 처리를 별도로 정의함 """
    def post(self, request):
        username = request.POST.get('username', '')
        if not username:
            return self.response(message='아이디를 입력해주세요!', status=400)
    
        password = request.POST.get('password', '')
        if not password:
            return self.response(message='비밀번호를 입력해주세요!', status=400)

        email = request.POST.get('email', '')
        try:
            validate_email(email)
        except ValidationError:
            return self.response(message='올바른 이메일을 입력해주세요!', status=400)            
        
        try:
            user = User.objects.create_user(username, password, email)
        except IntegrityError:
            return self.response(message='이미 존재하는 아이디입니다!', status=400)

        return self.response({ 'user.id' : user.id })


class UserLoginView(BaseApiView):

    def get(self, request):
        return self.response

    def post(self, request):
        username = request.POST.get('username') 
        if not username:
            return self.response(message='아이디를 입력해주세요!', status=400)
        
        password = request.POST.get('password')
        if not password:
            return self.response(message='비밀번호를 입력해주세요!', status=400)
        
        user = authenticate(request, username=username, password=password)
        if user is None:
            return self.response(message='일치하는 회원정보가 없습니다!', status=400)
        login(request, user)
        
        return self.response

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
@method_decorator(csrf_exempt, name='dispatch')
class BaseApiView(View):
    @staticmethod
    def response(data='{}', message='', status=200):
        result = {
            'data' : data,
            'message' : message
        }
        return JsonResponse(result, status=status)


class UserCreateView(BaseApiView):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(UserCreateView, self).dispatch(request, *args, **kwargs)

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
            # user = User.objects.create_user(username, password, email)
            ''' create_user : parameter 순서에 주의하자.
            1. parameter 순서대로 기입하거나 
            2. 명시적으로 이름과 값을 매핑하여 입력하거나 '''
            # user = User.objects.create_user(username, email, password)
            user = User.objects.create_user(username=username, password=password, email=email)
        except IntegrityError:
            return self.response(message='이미 존재하는 아이디입니다!', status=400)

        return self.response({'user.id' : user.id}, message='정상처리되었습니다.')


class UserLoginView(BaseApiView):
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
        
        return self.response(message='정상처리되었습니다.')


class UserLogout(BaseApiView):
    def get(self, request):
        logout(request)
        return self.response(message='정상처리되었습니다.')


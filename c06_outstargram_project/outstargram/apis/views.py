from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.validators import validate_email, ValidationError

from contents.models import Content, Image, FollowReleation

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


@method_decorator(login_required, name='dispatch')
class ContentCreateView(BaseApiView):
    def post(self, request):
        text = request.POST.get('text', '').strip()
        content = Content.objects.create(user=request.user, text=text)
        for idx, file in enumerate(request.FILES.values()):
            Image.objects.create(content=content, image=file, order=idx)
        return self.response(message="정상처리되었습니다.")


@method_decorator(login_required, name='dispatch')
class RelationCreateView(BaseApiView):
    def post(self, request):
        try:
            followee_id = request.POST.get('id')
        except ValueError:
            return self.response(message='잘못된 요청입니다.', status=400)

        relation, is_created = FollowReleation.objects.get_or_create(follower=request.user)

        try:
            if followee_id == request.user.id:      # 자기 자신을 follow 방지
                raise IntegrityError
            relation.followee.add(followee_id)
            relation.save()
        except IntegrityError:
            return self.response(message='잘못된 요청입니다!', status=400)

        return self.response(message='정상처리되었습니다.')
    
        
@method_decorator(login_required, name='dispatch')
class RelationDeleteView(BaseApiView):
    def post(self, request):
        user = request.user

        try:
            followee_id = request.POST.get('id')
        except ValueError:
            return self.response(message='잘못된 요청입니다.', status=400)

        try:
            relation = FollowReleation.objects.get(follower=user)
        except FollowReleation.DoesNotExist:
            return self.response(message='잘못된 요청입니다!', status=400)
        
        try:
            if followee_id == user.id:
                raise IntegrityError
            relation.followee.remove(followee_id)
            relation.save() 
        except IntegrityError:
            return self.response(message='잘못된 요청입니다!', status=400)

        return self.response(message='정상처리되었습니다.')


@method_decorator(login_required, name='dispatch')
class UserGetView(BaseApiView):
    def get(self, request):
        username = request.GET.get('username', '').strip()

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return self.response(message='검색결과가 없습니다!', status=400)        
        return self.response(message='정상처리되었습니다.', data={'id':user.id, 'username':user.username, 'email':user.email})

from django.shortcuts import render
from .models import NewUser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        # userEmail = request.POST['userEmail']   
        # userPw = request.POST['userPw']
        # userRePw = request.POST['userRePw']

        # if userPw != userRePw:
        #     return HttpResponse('비밀번호가 다릅니다! ')

        userEmail = request.POST.get('userEmail', None)   
        userPw = request.POST.get('userPw', None)
        userRePw = request.POST.get('userRePw', None)

        res_data = {}

        if not (userEmail and userPw and userRePw):
            res_data['error'] = '모든 값을 입력해야합니다!'
        elif userPw != userRePw:
            res_data['error'] = '비밀번호가 다릅니다!'
        else:
            newuser = NewUser(
                username=userEmail,
                password=make_password(userPw)
            )

            newuser.save() 

        return render(request, 'register.html', res_data)

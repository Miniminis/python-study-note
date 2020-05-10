from django.shortcuts import render, redirect
from .models import NewUser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm

# Create your views here.
def home(request):
    user_id = request.session.get('user')

    res_data = {}
    if user_id:
        username = NewUser.objects.get(pk=user_id)
        res_data['username'] = username

    return render(request, 'index.html', res_data)   

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else :
        form = LoginForm()      # GET 
            
    return render(request, 'login.html', {'form' : form})   

# def login(request):
#     if request.method == "GET":
#         return render(request, "login.html")
#     elif request.method == "POST":

#         userEmail = request.POST.get('userEmail', None)
#         userPw = request.POST.get('userPw', None)

#         res_data = {}
#         if not (userEmail and userPw):
#             res_data['error'] = '모든 값을 입력해야합니다!'
#         else:
#             newuser = NewUser.objects.get(useremail=userEmail)
#             if check_password(userPw, newuser.password):
#                 request.session['user'] = newuser.useremail
#                 return redirect('/')
#             else:
#                 res_data['error'] = '아이디 혹은 비밀번호를 확인해주세요!'

#         return render(request, "login.html", res_data)


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

        
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        # userEmail = request.POST['userEmail']   
        # userPw = request.POST['userPw']
        # userRePw = request.POST['userRePw']

        # if userPw != userRePw:
        #     return HttpResponse('비밀번호가 다릅니다! ')

        userName = request.POST.get('userName', None)
        userEmail = request.POST.get('userEmail', None)   
        userPw = request.POST.get('userPw', None)
        userRePw = request.POST.get('userRePw', None)

        res_data = {}

        if not (userName and userEmail and userPw and userRePw):
            res_data['error'] = '모든 값을 입력해야합니다!'
        elif len(userName) <2 or len(userName) >6:
            res_data['error'] = '닉네임은 2자에서 6자 사이로 입력해주세요!'
        elif userPw != userRePw:
            res_data['error'] = '비밀번호가 다릅니다!'
        else:
            newuser = NewUser(
                username=userName,
                useremail=userEmail,
                password=make_password(userPw)
            )

            newuser.save() 

        return render(request, 'register.html', res_data)
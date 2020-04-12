###
# Python 3.8.1
# Django 3.0.3
###

## 파이썬 프로젝트 설정 in vscode 
# Extentions
# 1. python 
# 2. python for vscode 

# # Command Pallete 
# 1. 가상환경세팅 
# 2. Python select Interpreter
# 3. Task:configure task > others > 설정파일 복붙


## pip commands
# pip install : pip로 파이썬 패키지(라이브러리) 설치하기
# pip uninstall : pip로 파이썬 패키지(라이브러리) 삭제하기
# pip freeze : pip로 설치한 파이썬 패키지(라이브러리) 목록 표시
# pip freeze > requirements.txt : 위의 목록을 requirements.txt 라는 파일로 만들기
# pip install -r requirements.txt : requirements.txt 안의 패키지 전체 설치하기

# django project 
# 1. 프로젝트 directory 만들기 
# 2. 가상환경 설정 : pip install virtualenv, vitrualenv [가상환경이름] || python -m venv [가상환경이름] 
# 2-1. 가상환경 활성화 : [가상환경이름]\scripts\activate
# 3. django 설정 : pip install django
# 4. project 생성 : django-admin startproject [project name]
# 5. app 생성 : cd [project name] >> django-admin startapp board    //각 기능별로 별도의 app으로 생성 

## (example) django project setting
# 새로운 폴더 생성 후 독립 환경 설정
# pip install --upgrade pip
# pip install django
# django-admin startproject baemin
# 가장 상단의 baemin 폴더 src 로 이름 변경
# python manage.py migrate
# python manage.py startapp client
# python manage.py startapp partner
# 기존 프로젝트에서 templates 폴더 만들고, base.html 복사하기
# 기존 프로젝트에서 static 폴더 통째로 복사하기
# baemin/settings.py 파일 안 세팅 수정하기 (기존 프로젝트 참고)
# INSTALLED_APPS 리스트 안에 'client', 'partner' 넣기
# TEMPLATES 안 'DIRS' 리스트 안에 os.path.join(BASE_DIR, "templates")
# 가장 하단에 STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static") ] 추가
# 깃허브에 프로젝트 올리기
# README.md 파일 만들고, git init 이후, git add . 로 전체 파일 추가하기
# .gitignore 파일 만들고, 아래 목록 각각 추가
# db.sqlite3
# baemin_sample/ (독립 환경 생성 시 만들어지는 폴더 이름)
# git commit -m "first commit" 부터 남은 설정 진행

## requirements.txt 에 있는 pip lib 한번에 설치하기 
# pip install -r requirements.txt 
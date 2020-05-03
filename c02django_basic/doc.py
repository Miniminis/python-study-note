"""
django framework 
- mvt : model, view, template layer 
- model : 데이터베이스와 연관 
- view : business logic
- template : html codes  
- form 
- admin 
- security and etc.

프로젝트 만들기 
- django-admin startproject [project name]
- cd [project name]
- django-admin startapp [분리된 기능/앱]

MTV (MVC pattern)

create new_community project
create board app
create new_user app

가상환경 설정 >> pip install django >> django-admin startproject >> django-admin startapp 

데이터베이스 설정 
- models.py : class 생성 
- console : python manage.py makemigrations : 클래스에 맞는 테이블 생성
- console : python manage.py migrate : 데이터 마이그레이션 >> db.sqlite3 생성됨
- sqlite db.sqlite3 ERROR 

session 

"""
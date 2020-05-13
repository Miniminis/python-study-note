"""
============================================
django framework 
- mvt : model, view, template layer 
- model : database 
- view : business logic
- template : html codes  
- form 
- admin 
- security and etc.
============================================

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

*** new_community app *** 
회원가입 
1. 템플릿 작성 - 상속 개념 사용해서 효율적으로 구성하기 
2. 모델
3. 뷰 
- validation check:
    - null or empty check 
    - db 값인지 확인 
4. url 연결

로그인 
1. 템플릿 
2. 뷰 
- validation : 1) null or empty 2) check_pw 
3. url 연결 

게시판 리스트 
1. 템플릿 작성 
- 게시글 목록 리스트 : 게시글 번호, 제목, 작성자, 작성시간 노출 
2. 모델 작성
- 게시글번호 : 자동생성
- 제목
- 작성자 : foreign key (new_user 의 username)
    - onDeleteCascade : default 값으로 설정하기 
- 작성시간 : 자동생성 
3. 뷰 연결 
4. url 연결 

게시판 글쓰기 
1. 템플릿 작성
- form  
2. form.py 
- null or empty check 
3. view 
- session check : useremail --> foreign key 
4. url 

게시판 상세 
1. template 
- form : read only
- pk - board 1개  
2. view.py 
- pk from url
- pass pk.board to template  
3. url 


"""
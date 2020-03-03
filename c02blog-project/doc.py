# django project 세팅 
# 1. mkdir, cd dir
# 2. pip freeze 
# 3. pip install virtualenv
# 4. python -m venv sample_env
# 5. sample_env\scripts\activate
# 6. pip freeze 
# 7. pip install django 
# 8. django-admin startproject [] - 전체 프로젝트 
# 9. django-admin startapp [] - 기능단위
# 10. python manage.py migrate - dbsqlite3 생성됨 : 로컬에서 쓸 수 있는 데이터 베이스가 생성됨 - 깃에서 업로드 제외


# MTV 구조 
# 1. blog urls 설정 - include  
# 2. feed urls 설정 - views 와 연결 
# 3. Views : render 페이지 설정 및 비즈니스 로직 
# 4. Templates : html page 
# 5. Models : db table 요소 및 구조 세팅 

# 로컬 서버 시작 : python manage.py runserver

# django admin setting : python manage.py createsuperuser

# 항상 models.py 수정 후, 
# 1. python manage.py makemigrations
# 2. python manage.py migrate

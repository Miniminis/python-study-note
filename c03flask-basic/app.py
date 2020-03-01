from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello, flask world!'



## 1. 가상환경 설정
# - pip install virtualenv
# - python -m venv []
# - []\scripts\activate

## 2. flask 설치
# - pip freeze 
# - pip install flask 
# - pip freeze > requirements.txt

## 3. flask app 작성해보기 
# - app.py 

# MVC Pattern 
# Model(DB와 연결) - View(클라이언트가 보는 화면) - Controller(접근 url 별로 비즈니스 로직 수행)

## SQLAlchemy in Flask 
# ORM (Orbject Relational Mapping) : 객체와 DB를 자동으로 매핑해 주는 것

## Persistance Framework 
# 영속성 : 데이터를 생성한 프로그램이 종료되더라도 데이터가 사라지지않고 저장되는 것
# 종류 : SQL Mapper 와 ORM 
# SQL Mapper : Mybatis,  
# ORM : JPA, Hibernate 등 

## 참고 : 
# - [[DB] ORM이란](https://gmlwjd9405.github.io/2019/02/01/orm.html)


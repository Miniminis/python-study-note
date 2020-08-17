---
title : fc_mall proejct
description : 쇼핑몰
---

# fc_mall project

## one-page-view

![image](fc_mall.png)

## 환경설정

- 가상환경생성 및 활성화
- django 설치
- django project 생성
- django app 생성 : user, product, order

## 데이터베이스 설계 - models.py

1. user
   1. email
   2. passwrod
   3. regdate
2. product
   1. name
   2. price 
   3. description
   4. stuck
   5. regdate
3. order
   1. user
   2. product
   3. quantity
   4. regdate

## 회원가입 (클래스 기반의 뷰)

1. template
   1. base
   2. index
   3. register
2. forms.py
3. url connect

## 로그인 - 클래스 뷰 이용

1. forms.py : class LoginForm 생성
2. view.py : class LoginView 생성
   1. validation check 
   2. session save
3. url connect 

## 상품리스트 - ListView

1. views.py : class ProductListView
   1. connect to model 
2. template : table 형태로 표현
3. urls connect

## 상품 상세

1. views.py : class ProductDetailView
2. tempalte: product_detail.html 
3. urls connect 

## 상품 등록

1. forms.py
2. views
3. templates 
4. url connect

## 주문하기

1. template 에서 url 연결 - form, post to orderForm
2. url 연결
3. orderCreateView 생성
   - orderForm 생성
   - success url 연결 
4. 주문 form 생성
   - user : foreign key. session 에서 가져와야함. --> session 필요 
   - product : hiddenInput 으로 detail page 에서 자동입력
   - quantity : 사용자가 직접 입력
5. product template 에서 orderForm 연결 
6. orderForm 에서 form_invalidate 시, 다시 product detail page 로 리다이렉트 
7. 주문결과 확인

## 주문 리스트 조회 

## Decorator 

- transaction management
- authority check

## form과 model의 분리 

- form : form field 정의 및 각 field data 의 유효성 검사를 수행
- view : 유효성 검사를 거친 정제된 데이터를 model에 데이터 저장

## drf : Django-Rest-Framework

- https://www.django-rest-framework.org/
- response page 의 단점 
   - 매번 새로운 페이지를 그려야 한다.
   - 다양한 플랫폼에 대응하지 못한다 : android, ios, web
   - client 와 server 가 서로 종속되어있어 client 입장에서는 다양한 화면을 그리기 어렵다.
- client 와 server 의 완전한 분리 
   - client : request : json data
   - server: response : json data, not page


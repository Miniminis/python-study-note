---
title : fc_mall proejct
description : 쇼핑몰
---

# fc_mall project

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

1. forms.py 
2. views
3. templates 
4. url connect



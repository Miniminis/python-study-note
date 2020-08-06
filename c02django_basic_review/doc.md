# django framework 

## framework?

- 자주 사용되는 코드를 체계화하여 쉽게 사용할 수 있도록 도와주는 코드 집합
- 라이브러리와 혼동될 수 있지만 좀 더 규모가 크고 프로젝트의 기반이 됨 
- 건축에 비유하자면 구조를 만드는 골조가 프레임워크라면, 그 이외의 자재들이 라이브러리가 됨

## MTV

- Model 계층: 데이터베이스 연동. python 의 경우는 ORM 지원.
    - 쿼리 
    - 모델 인스턴스
    - raw query
- Template 계층
    - html code 
- View 계층: 비즈니스 로직
    - url parsing. 내부에 변수도 사용 가능
    - decorator 
    - request, response

## 가상환경 세팅, django framework 설치

1. 가상환경 설정
    - pip install virtualenv
    - python -m venv  [가상환경이름]
    - [가상환경이름]\Scripts\activate
2. django framework 설치 
    - pip install django
    - django-admin startproject [project name]
    - django-admin startapp [app name] : app 은 기능 단위로 분리

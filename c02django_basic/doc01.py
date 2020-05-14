"""
============================================
django 실전개요 : 쇼핑몰
1. 클래스를 활용한 뷰 생성 
    - 함수와 클래스 : 뷰의 재사용
    - 데코레이터 : 기능의 재사용 
2. drf로 restful api 개발 
============================================

1. 프로젝트, admin, app 생성
    - 사용자 app
    - 상품 app
    - 주문 app
2. 모델 : 
    - 사용자 : 이메일, 비번, 가입시간
        - 메타 클래스 : 
        - db_table, verbose_name, verbose_name_plural
    - 상품 : 이름, 가격, 설명, 재고, 등록시간
        - 메타 클래스 : 
            - db_table, verbose_name, verbose_name_plural    
    - 주문 : 외래키(사용자)-ondelete 속성설정, 외래키(제품)-ondelete, 주문날짜시간, 수량
        - 메타 클래스 : 
            - db_table, verbose_name, verbose_name_plural
3. settings.py : installed_apps 에 세 개의 앱 추가
4. 데이터 마이그레이션 

5. django admin 추가 
- 각 app 별로 admin 설정
- createsuperuser : python manage.py createsuperuser
- in model : __str__ 값 커스텀 
6. 클래스 기반으로 뷰 작성하기 : 규칙 익히기 
7. index page 
- url 
- view 
- template : base, index
8. register page 
- url
- form
- view
- template 


"""
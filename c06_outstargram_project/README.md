# Out_Stargram_Project


## environment setting

- virtual env
- django install
- create django project
- timezone & language


## Function View vs. Class Based Bivew(CBV)

- 함수형뷰
    - if 문으로 get, post 등 매서드별로 분기처리 
    - 404 등 에러 페이지 이용가능 
- 클래스뷰
    - http method 별 처리시 매서드 명을 사용함으로써 가독성이 높아지고, 보다 깔끔해짐
    - 제너릭뷰, 믹스인 : 개발 생산성과 코드 재사용성이 높아짐


## modeling

1. user
    - name
    - email
    - password
2. content
    - user
    - text
3. image
    - content
    - image(path)
    - order
4. relation
    - followee : 1to1
    - follower : 1to1


## follow/unfollow

1. 나를 팔로우 하는 사람들
    - [follow] 버튼 show : 2번에 없는 사람들
2. 내가 팔로우 하는 사람들
    - [unfollow] 버튼 show : all ppl


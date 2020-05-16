"""
=================================================
language : python 
framework : scrapy 
site : google play store 
data to collect: 
    - app version
    - new comment
    - playstore 정책 업데이트
    - apk 전환율 : 버전별 숫치 
data save : 
    - crepass mail, gmail 로 하루에 한 번 전송
=================================================


process 
0. spider 생성
    - url 설정 : https://play.google.com/apps/publish/?hl=ko
    - 하루에 1번 크롤링 

1. admin 계정으로 로그인 >> 콘솔메인에서 앱 클릭
2. 앱 업데이트 체크  
    - apk 버전 관리 탭으로 클릭 >> 이동 
    - 출시관리 > 앱버전 
        Product item 
        1. 출시버전
        2. 버전코드 
3. apk 전환율 체크
    - 통계 > 앱버전 
    - 하단의 데이터 표 크롤링
        - 날짜, 버전, 숫, 비율  
4. 정책 업데이트 체크 
    - 상단 알림 아이콘 클릭 > "개발자 프로그램 정책 변경사항 확인" 
        - 업데이트 내용 메시지 
        - "자세히 알아보기" 링크 같이 전송 
5. 새 코멘트 체크 
    - 사용자 의견 > 리뷰 리스트 
        1. 날짜
        2. 작성자
        3. 내용 
        4. 답변 여부
        5. 링크        
6. scrapy 배포
"""



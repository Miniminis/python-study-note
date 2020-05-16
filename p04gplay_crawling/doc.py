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
    crepass mail, gmail 로 하루에 한 번 전송
=================================================


process 
1. admin 계정으로 로그인
2. google play console 접속
3. apk 버전 관리 탭으로 클릭 >> 이동 
4. 현재 버전 가져오기 
5. 반복 수집 : 
    - 현재버전에서 버전 비교
    - 버전 변화가 있다면 콘솔에 메시지 출력 
    - 메일 보내기
    - 현재버전 변수 업데이트 
"""



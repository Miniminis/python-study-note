
"""
평균, 분산, 표준편차를 함수로 만들기 
분산 : 산포도를 구하는 방법 중 하나. (점수 - 평균점수)**2 의 평균
표준편차 : 분산의 제곱근
"""

import openpyxl
import math

raw_data = {}
wb = openpyxl.load_workbook('cs06_class_2_3.xlsx')  # 엑셀 파일 로드
ws = wb.active  # 활성 시트 가져오기 
g = ws.rows  # 활성 시트의 행 모음
for name, score in g:
    raw_data[name.value] = score.value  # 각 행의 1열 name 은 key, 2열인 score 는 value 로 딕셔너리에 저장하기

scores = list(raw_data.values())  # value 인 score 만 모아서 리스트로 생성 

s = 0

for score in scores:  # 모든 점수 더하여 모든 학생의 총 점수 구하기 
    s += score

avrg = round(s/len(scores), 1)  # 전체 평균 점수 

s= 0

for score in scores:
    s += (score - avrg) ** 2  

variance = round(s/len(scores), 1)  # 분산

std_dev = round(math.sqrt(variance),1)  # 표준편차 

print("평균: {0}, 분산: {1}, 표준편차: {2}".format(avrg, variance, std_dev))

if avrg <50 and std_dev >20:  # 각 평균점수와 표준편차에 따라서 다른 메시지 출력해주기 
    print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
elif avrg > 50 and std_dev >20:
    print("성적은 평균 이상이지만 학생들이 실력 차이가 크다. 주의 요망!")
elif avrg < 50 and std_dev <20:
    print("학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!")
elif avrg > 50 and std_dev <20:
    print("성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.")


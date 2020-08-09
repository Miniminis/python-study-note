
"""
함수를 이용하여 절차 지향으로 프로그램 바꿔보기
"""

import openpyxl
import math

def get_data_from_excel(filename):
    raw_data = {}
    wb = openpyxl.load_workbook(filename)  # 엑셀 파일 로드
    ws = wb.active  # 활성 시트 가져오기 
    g = ws.rows  # 활성 시트의 행 모음
    for name, score in g:
        raw_data[name.value] = score.value  # 각 행의 1열 name 은 key, 2열인 score 는 value 로 딕셔너리에 저장하기

    return raw_data


def average(scores):
    s = 0

    for score in scores:  # 모든 점수 더하여 모든 학생의 총 점수 구하기 
        s += score

    avrg = round(s/len(scores), 1)  # 전체 평균 점수 

    return avrg


def variance(scores):
    s= 0

    for score in scores:
        s += (score - avrg) ** 2  

    variance = round(s/len(scores), 1)  # 분산
    
    return variance

def std_dev(variance):
    std_dev = round(math.sqrt(variance),1)  # 표준편차 
    return std_dev


def print_msg(avrg, variance, std_dev):
    print("평균: {0}, 분산: {1}, 표준편차: {2}".format(avrg, variance, std_dev))

    if avrg <50 and std_dev >20:  # 각 평균점수와 표준편차에 따라서 다른 메시지 출력해주기 
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > 50 and std_dev >20:
        print("성적은 평균 이상이지만 학생들이 실력 차이가 크다. 주의 요망!")
    elif avrg < 50 and std_dev <20:
        print("학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!")
    elif avrg > 50 and std_dev <20:
        print("성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.")

if __name__ == "__main__":
    
    raw_data = get_data_from_excel('cs06_class_2_3.xlsx')
    scores = list(raw_data.values())

    avrg = average(scores)
    variance = variance(scores)
    deviation = std_dev(variance)

    print_msg(avrg, variance, deviation)


"""
함수들의 이름만 보아도 이 프로그램이 무슨 일을 하는 프로그램인지 한 눈에 파악할 수 있다. 
함수의 구현 내용을 몰라도 함수의 이름만 가지고도 프로그래머가 필요한 기능들을 가져다가 쓸 수 있다. 
"""


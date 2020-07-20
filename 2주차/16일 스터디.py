# 약속된 form으로 data 저장하기
# pickle 이용
# list, dic 내 마음대로 저장하고 불려올 수 있음
# 파일입출력, File IO
# **book 써보기, 원넓이
# base 서열 반만 읽기
# 계산기 매개변수 추가하여 입출력 하기 (보류)

# 원의 면적
def area(ban):
    PI = 3.141592
    #코드 안에 상수가 있으면 변수 지정을 통해 설명이 용이하도록 한다
    result = (ban**2)*PI
    return result

print(area(2))

# **book
def print_all(*a, **b):
    print(a)
    print(b)

print_all(1, 2, A ='Russian',  B = 'Asian' )

# base 서열 반만 읽기

# 원주율

import random
n = 100000
cnt = 0
for i in range(n):
    x = random.random()
    y = random.random()
    if ((x**2)+(y**2) < 1):
        cnt += 1
a = 4*cnt/n
print(a)
# %.2f 소숫점 2째 자리까지

# 달력

def cal(mon):
    print('\t'*2+'< 2020. ',mon,'>')
    l_cal = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start_frist = l_cal[mon-1] % 7
    print('\t'*start_frist, end = '')
    for i in range(1, l_cal[mon-1]+1):
        if start_frist == 6:
            start_frist = 0
            print(i)
        else:
            start_frist += 1
            print(i, end = '\t')

cal(3)

# 희재

#day = 3
#flag = 0
#l_cal = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#mon = 6

#for i in range(mon - 1) :
#    day += l_cal[i] # input 월의 날짜 수

#day %= 7 # 1일의 요일을 정함(앞에 공백 갯수 정함)
# [0] 일 ~ [6] 토

#for i in range(1, l_cal[mon - 1] + 1) :
#    if flag == 0:
#        print("\t" * day, end = "") # 달력 앞 공백
#        flag = 1 # 다시 여기로 안돌아올거임
#    if day % 7 == 6 : # 토요일의 마지막 숫자 적고 다음 줄
#        day = 0
#        print(i)
#    else: # 숫자를 넣고 사이는 탭으로 구분
##        print(i, end = "\t")

# 모듈

# import 모듈
# from 모듈 import *
# from 모듈 import 함수명
# from 모듈 import 클래스

l_list = [ 'a', 'a', 'b', 'c' ]
#import collections     collections 안에 있는 모든 함수를 가져옴
from collections import Counter # Counter만 가져옴

#cnt = collections.Counter(l_list)
cnt = Counter(l_list)
print(cnt)

e = 'variable e'
print(e)

from math import *
print(e)
print(pi)

import math
print(math.e)
print(math.pi)
print(math.sqrt(16))

from math import e
print(e) # 출력
print(pi) # 출력 X

import math as m
print(m.e)
print(m.pi)

from math import pi as p
print(p)

# 왠만하면 이미 만들어지 생명정보 데이터 처리 프로그램 사용
# python으로 새로 짠다면
# pip, conda 패키지 매니저 -> 패키지 설치 -> pandas, numpy
# -> 바이오파이썬, faidx?? 등 사용함

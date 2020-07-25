# line3의 s_str을 이용하여 각 단어의 개수를 출력하세요

s_str = 'We tried list and we tried dicts also we tried Zen'
s_list = s_str.split(' ')

import collections
s_dic = collections.Counter(s_list)
print(s_dic)

for key in s_dic.keys():
    print(key, s_dic[key])

for k, v in s_dic.items():
    print("{0}\t{1}".format(k, v))

# 정삼각형 만들기

#line = input(input("Star line: "))
line = 3
for i in range(1, line+1):
    print(' '*(line-i)+'*'*(2*i-1))

# 랜덤 25 숫자 오름차순으로 5개씩 리스트 삽입 및 5줄로 추출
import random
ran = random.sample(range(0,100), 25)
print(ran)

ran_sor = sorted(ran)
print(ran_sor)

ran_result = []
for i in range(0, len(ran_sor), 5):
    ran_tmp = ran_sor[i:i+5]
    ran_result.append(ran_tmp)
for x in ran_result:
    print(x)

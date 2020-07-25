# line3의 s_str을 이용하여 각 단어의 개수를 출력하세요

s_str = 'We tried list and we tried dicts also we tried Zen'

list = s_str.split(' ')
set1 = set(list)
set_list = []
for i in set1:
    set_list.append(i)

print('word list:', set_list)

for i in range(len(set_list)):
    print(set_list[i], list.count(set_list[i]))

# 승민이 형
d_str = {}
l_str = s_str.split(' ')
for i in range(len(l_str)):
    k = l_str.count(l_str[i])
    d_str[l_str[i]] = k
for i in d_str.keys():
    print(i, d_str[i])

# 희재
s_dic = {'We':1, 'we':2, 'tried':3, 'list':1, 'and':1, 'dicts':1, 'also':1, 'Zen':1}
for k, v in s_dic.items():
    print("{0}\t{1}".format(k, v))

# 정답안
l_str = s_str.split(' ')
for i in l_str:
    print(i)

d_cnt = {}

for i in l_str:
    if i not in d_cnt:
        d_cnt[i] = 1 #단어의 개수 지정
    else:
        d_cnt[i] +=1 #key가 중복될 시 값에 +1을 하라
print(d_cnt)
for k, v in d_cnt.items():
    print("{0}\t{1}".format(k, v))

# colliections.Counter() 써보기
import collections
cnt = collections.Counter(l_str)
print(cnt)

A = ['a', 'b', 'a', 'c', 'd', 'f']
B = ['b', 'c', 'b', 'd', 'e', 'e', 'e']
C = ['q', 'w', 'e', 'r', 't', 'y', 'y', 'y']

a_cnt = collections.Counter(A)
b_cnt = collections.Counter(B)
c_cnt = collections.Counter(C)

print(a_cnt)
print(b_cnt)
print(c_cnt)

a_cnt['a'] += 5 # 'a' key의 value에 5를 더함

print(a_cnt)
print(a_cnt | b_cnt) # 합집합 (큰수부터 정렬)
print(a_cnt - b_cnt) # 차집합
print(a_cnt & b_cnt) # 교집합 ('b':1이 남은 이유는 두 사람이 가진 'b'의 개수 중 공통적으로 1를 가지기 때문)

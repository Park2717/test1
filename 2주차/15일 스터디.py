# 짝수 줄 출력
s_str = "Bravely bold Sir Robin rode forth from Camelot\nYes, brave Sir Robin turned about\nHe was not afraid to die, O brave Sir Robin\nAnd gallantly he chickened out\nHe was not at all afraid to be killed in nasty ways\nBravely talking to his feet\nBrave, brave, brave, brave Sir Robin\nHe beat a very brave retreat"

s_split = s_str.split("\n")

for i in range(len(s_split)):
    if i % 2 == 1 :
        print(s_split[i])

# 정삼각형 만들기
dic = {1:3, 3:2, 5:1, 7:0}

cnt = 0
while cnt < 7 :
    cnt += 1
    if cnt % 2 == 1 :
        tri = "*"*cnt
        print(' '*dic[cnt],tri)
    else :
        continue

# 승민이 형
line = int(input("star line : "))
for i in range(1, line+1):
    print(' '*(line-i)+'*'*(2*i-1)

# 랜덤 25 숫자 오름차순 5개씩 리스트 정렬, 5줄 추출
import random
ran = []
cnt = 0
while cnt < 25 :
    cnt +=1
    ran.append(random.randint(0, 100))
    continue
print(ran)
ran_sor = sorted(ran)
l_result = []
for i in range(0, len(ran_sor), 5) :
    l_tmp = ran_sor[i : i + 5]
    l_result.append(l_tmp)
for x in l_result :
    print(x)

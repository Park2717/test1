# 함수를 이용하여 피보나치 수열을 계산
# F0 = 0, F1 = 1, F2 = F0 + F1 = 0 + 1 = 1
# 입력값 : 8, F7을 구하세요, 결과값 : 13
# 0 1 1 2 3 5 8

def pibo(number):
    num = []
    for i in range(0, number):
        if i < 2 :
            #num += [i]
            num.append(i)
        else :
            #num += [num[i-1]+num[i-2]]
            num.append(num[i-1]+num[i-2])
    print(num) # 출력 [0, 1, 1, 2, 3, 5, 8, 13]
    return num.pop()
test = pibo(1)
print(test) # 출력 13

# 정답안
l_pivo = [0,1]
#pivoIn = input('n_th pivo: ')
pivoIn = '8'
pivoIn = int(pivoIn)

for i in range(pivoIn-2):
    l_pivo.append(l_pivo[-1] + l_pivo[-2])
print(l_pivo[-1])

#def 논문요약쌉가능(nonmoon):
#    result = [텅텅]
#    if 'you have money' = True:
#        result.append(nonmooon.fllito(전문가한테 견적받기))
#    else:
#        result.append(nonmoon.구글링(노오옹력))
#    print(result)
#try = 논문요약쌉가능(논문해석하기싫어)
#print(try, '교수님 죄송합니다')

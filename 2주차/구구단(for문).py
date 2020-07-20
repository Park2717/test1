# 구구단 출력하기
dan = 4
while True:
    #dan = int(input('give me dan: '))
    if not dan.isdigit():
        continue
    elif 2 <= int(dan) <= 19:
        break
print(dan, 'Dan')
print()
for i in range(1, 20) :
    print(dan*i, end = ' ')
    if i == 10:
        break

print('-'*10)

dan = 2
if 19 >= int(dan) >= 2 :
    for i in range(1, 10) :
        num = dan*i
        print (dan,'x',i,'=',num)
    else:
        print('no')

# print("{0} X {1} = {2}".format(num, i, num * i)) 으로도 출력 가능

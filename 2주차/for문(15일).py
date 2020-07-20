for i in ['apple', 'peach', 'banana']:
    print('there is an {0} in basket!'.format(i))

cnt = 0
for i in [1, 2, 3, 4] :
    cnt +=i
print(cnt)
print('-'*10)

cnt = 0
for i in [1, 2, 3, 4] :
    if i == 2:
        continue
    cnt +=i
print(cnt)
print('-'*10)

# list(range(3)) -> [0, 1, 2] 출력 <- for문에서 자주 사용함
# list(range(0, 10, 2)) 0 ~ 10 까지 2씩 증가해서 추가됨 (끝 값은 안나옴)

cnt = 0
for i in range(5) : # 얼마나 명령이 시행될 것이냐
    cnt +=1 # 다음 명령 시행에서 cnt에 1을 더해서 출력할거다
    print('for loop', cnt, 'tried') # range가 5번이니 cnt가 5까지 출력이 된다

print('-'*10)

cnt = 0
l_list = [1,2,3,4]

for i in l_list:
    cnt += i
print(cnt)

print(sum(l_list))
print('-'*10)

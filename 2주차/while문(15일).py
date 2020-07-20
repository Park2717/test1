cnt = 0
while True: # while문은 true일때만 시작이 된다
    print("while test!\t", cnt)
    cnt +=1
    if 5 < cnt :
        print("cnt >5!", cnt)
        break
    elif 2 < cnt: # 3 4 5 가 들어가는 곳
        print("continue!")
        continue # while문 안에서 실행이 되면 while문을 바로 나가지만 break가 아닌 다시 처음부터 반복시킨다.
    print("while test!\t", cnt) #이건 if문 밖에 있는데 3 4 5 출력이 안됨 왜일까?
print("Done!")

cnt = 0
while cnt < 5:
    print("cnt:", cnt)
    cnt +=1
    print("cnt_2:", cnt) # 다시 while문에 들어가기 전에 변환된 5로 출력이 되고 while문이 끝나게 된다.

cnt = []
while 1 :
    print("cnt:", cnt)
    cnt +='*'
    if cnt.count('*') > 5 :
        print("triangle", end = ' ')
        break
    elif cnt.count('*') <= 5 :
        continue
print("Complete")

# while not = if 랑 동일하기 때문에 if 줄을 굳이 안써도 된다

cnt = 2
while (cnt < 5) and (1<cnt):
    print('*'*cnt)
    cnt +=1

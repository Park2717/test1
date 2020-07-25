# 파이썬에서는 함수 결과값을 여러개 출력할 수 있다

def fruitTree(fruit): # 함수명(매개변수)
    print('fruit:', fruit)
    return fruit + ' tree'

fruitTree('apple') # fruit에 apple이 들어감

tree = fruitTree('peach') # 함수 작업을 변수에 넣어줌
print(tree) # return 값이 나옴

def add(a, b): # 매개변수 a, b
    print('add', a, 'and', b)
    print('%d + %d ='%(a,b), a+b) #
    return a, b, a+b # 결과값 a + b, a, b

A, B, result = add(3, 4) # tuple이 아닌 따로 따로 저장
print(A)
print(B)
print(result)
print('-'*10)

result = add(3, 4) # 인수
print('-'*10)
print('result:', result) # 결과값이 tuple로 묶여있다

def hello(): # 매개변수가 없음
    print("Hello!") # 결과값이 없는 함수

hello()
print('resHello start')
res_hello = hello()
print('res_hello:', res_hello) # None이 출력됨 함수에서 변수값이 없기 때문
print('resHello end')

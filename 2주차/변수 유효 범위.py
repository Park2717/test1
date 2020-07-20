#지역 변수 local variable
#-	함수 내에 선언된 변수
#-	함수 내에서만 사용
#전역 변수 global variable
#-	함수 외부에 선언된 변수
#-	함수 외부에서 사용 가능
#-	global 이용하여 함수 내에서 접근 가능
#특정 함수에서만 사용되는 값은 지역 변수로 선언


#def hihi(a, b, c): #c는 필요없는 매개변수 (메모리가 사용되기에 지우는게 좋음)
#    print(a)
#    print(b)
#    return a+b

#hihi('hi', 'hello') #함수 호출, 인자 인식
#a = 'hihi'
#b = 'hello'
#함수 내 선언된 변수 (지역 변수)
#print(a)쓰면 'a'라는 변수를 못찾음(a는 hihi함수의 지역 변수이기 때문)
# 지역 변수를 쓰면 a라는 변수를 저장하는데 메모리를 쓰지 않음
# 함수 안에서만 사용되기 때문에 함수 쓸때만 a가 메모리에 저장됨

def hihi(a, b):
    c = 'This is C'
    print(a)
    print(b)
    print(c)
    return a+b, c #지역 변수를 전역 변수로 가져오게 됨

a, c = hihi('hi', 'hello')
# 순서만 맞춰지면 데이터를 안과 밖으로 주고 받을 수 있음
print('-'*10)
a, c = hihi(b = 'hi',a = 'hello')
# 함수 순서를 지정할 수 있음
print('-'*10)
print(a)
print('-'*10)
print(c)


chicken = 10
def cChicken(people):
    chicken = 20
    chicken -= people
    print('cCkiecken_print:', chicken)

def countChicken_global(people):
    global chicken
    #global 명령어를 사용하여 전역 변수인 chicken을 지역 변수로 가져옴
    chicken -= people
    # chicken = chicken - people
    print('{0} chicken remained.'.format(chicken))

print('chicken:', chicken)
cChicken(people = 5)
print(chicken) # 독립적인 변수를 만들어서 사용했기 때문에 지역 변수는 변동 X
countChicken_global(5)
print(chicken) # 전역 변수에 영향이 갔음
# global은 명확한 목적이 있지 않는한 자주 사용하지 않는 것이 좋다

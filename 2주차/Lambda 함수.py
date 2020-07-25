def book(name, age, *book):
#*book은 뒤에 매개변수 개수를 제한하지 않음을 의미 (뒤에 오는 매개변수를 book 매개변수로 지정)
    print(name, age, end = ' ')
    for i in book:
        print(i, end = ' ')
    print() # 엔터 역할
    return name

name1 = book('name1', '100', 'C', 'C++')
print('name1:', name1)

name2 = book('name2', '100', 'C', 'C++', 'Python')
# 매개변수 초과지만 *book을 썻기 때문에 가능
print('name2:', name2)

# **book 스터디 하기
# **dic

# lambda 사용하기 (짧은 함수에 자주 사용)
i_lambda = (lambda x, y: x + y)(3, 4)
# 함수명과 결과값 필요 x, 매개변수와 결과값 한 line에 작성
print(i_lambda)

def SUM(x, y):return x+y
i_func = SUM(3, 4)
# 함수는 2줄
print(i_func)

# 연습문제 간단한 계산기 만들기
result = 0
def calc(num0, num1, operator):
    if operator == '+':
        result = num0 + num1
    elif operator == '-':
        result = num0 - num1
    elif operator == '*':
        result = num0 * num1
    elif operator == '/':
        result = num0 / num1
    else: print("No")
    return result
num = calc(3, 5, '*')
print(num)

def calc(num0, num1, operator):
    result = eval(num0+operator+num1)
#    print(num0+operator+num1)
    return result
Result = calc('4', '5', '*')
#print('{}is result.'.format(calc(num0,num1,operator)))
# 이렇게 print 하면 계산기를 두번 사용해야하기 때문에 이렇게 쓰지 말자
print('{0} is result.'.format(Result))

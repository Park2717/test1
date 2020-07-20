# class는 c언어에서 없지만 편하기 때문에 존재
# 스터디 때 연습문제 풀어보기

# 클래스 : 함수와 데이터를 함께 관리
# 프로그램의 코드를 재사용하기 편함

# 속성(attribute) : 클래스의 변수
# 메소드(method) : 클래스의 함수

# 객체
# 인스턴스

# 객체지향 프로그래밍
# 대규모 프로그램 개발

## 예시

# 클래스 : Person 주로 대문자로 시작
# 속성 : nation
# 메소드 : greeting, printNation, chageNation

# 추상화
           #1반 2반 3반
l_coffee = [10,  8,  3]

for i in range(len(l_coffee)):
    print('There are', l_coffee[i],'in', i+1, 'class')

print('-'*30)

# class는 변수와 함수를 함께 가지고 있음
class Coffee():
    numCoffee = 10
    def Hello(self):
        # 매개변수 란에 self라고 쓰기
        # 이 함수가 실행이 될 때 group1_coffee의 정보를 self로 받는 거임
        print('Hello')
        return "Hi!"

group1_coffee = Coffee()
group2_coffee = Coffee()
# 객체 group1_coffee 이다.
# Coffee의 인스턴스(instance)인  group1_coffee 이다.
print(group1_coffee.numCoffee)

print(group2_coffee.numCoffee)
# group1_coffee의 속성인 numCoffee 변수를 가져옴 ## 10
# group2_coffee의 속성인 numCoffee 변수를 가져옴 ## 10
print('-'*30)

print(group1_coffee.numCoffee) #10
out = group1_coffee.Hello() # Hello
print(out) # Hi

print('-'*30)


class Person: # class 이름은 대문자가 좋음!
    nation = 'A nation'
    def greeting(self):
        print('greeting!')
    def printNation(self):
        print(self.nation)
    def chageNation(self, target):
        self.nation = target
        print('changeNation to {}'.format(target))

yune = Person()
#yune.nation
print(yune.nation)
print(yune.printNation) # 에러 : method가 나옴
yune.greeting() # greeting
yune.printNation() # self.nation
yune.chageNation('Korea') # Korea
yune.printNation() # 출력 X

#yune이 Person class의 인스턴스인가?
if isinstance(yune, Person):
    print('yune is Person')
else:
    print('yune is not Person')

# 검사용도
# 1이라는 객체가 int or str인가?
out0 = isinstance(1, (int, str))
out1 = isinstance('aa', int)
print(out0)
print(out1)

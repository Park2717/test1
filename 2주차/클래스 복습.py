class Person():
    s_str1 = 'str1'
    s_str2 = 'str2'
    def prtStr(self):
        out = self.s_str1 + self.s_str2
        print(out)
    def showS_str1(self):
        print(self.s_str1)

p1 = Person()
# p1.s_str1+='aa'   # 이렇게 안씀 (class의 변수를 바꿔버림)
# class를 쓰는 이유는 class를 수정하지 않고 연산하고 출력만 가져오도록 하는 것이다.

p1.showS_str1()    # 이렇게 씀
# print(p1.s_str1) # 이렇게 안씀
p1.prtStr()

class Person:
    nation = 'A nation'
    def greeting(self): #method
        print('(method)greeting:', 'Hi')

    def hi1(self):
        self.greeting()
    def hi2(self):
        greeting()

def greeting(): #function
    print('(function)greeting:', 'Hello')

yune = Person()
yune.greeting()
print()
yune.hi1() # method를 실행
yune.hi2() # function을 실행

# self -> 메소드를 실행한 객체
#!!메소드에서!!
#self가 있다 -> 객체가 있다 -> 객체의 속성 접근가능

## 용어 정리
# 클래스. Person
# yune 객체
# Person 클래스의 인스턴스 yune

# yune = Person()
# yune.hi() <- 메소드
# yune.name <- 속성
# yune.__age <- 비공개속성 .. 에러남
# Person class의 메소드 내에서 self.__age로 접근해야 함

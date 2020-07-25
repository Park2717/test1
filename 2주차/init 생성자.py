a = 3 #a를 3으로 초기화 시킴

class Person():
    nation = 'A nation'
    def __init__(self, country):
        self.nation = country
    def showNation(self):
        print(self.nation)

yune = Person('Korea') # yune 생성 -> __init__
# country 매개 변수에 Korea를 넣음
yune.showNation()


## 상속
#class 자식클래스(부모클래스):
#부모클래스의 모든 맴버를 상속받음

class Cat:
    def __init__(self):
        self.sleepy = True
    def snack(self):
        print('myeo~')

class KoShort(Cat): #class 안에 class 삽입 (상속)
#Cat에 있는 초기화 정보를 모두 가져옴
    def snack_Kor(self):
        print("muuu")

minyong = KoShort()
print()
minyong.snack()
minyong.snack_Kor()
print()
print(minyong.sleepy)

# 객체 4개
# 부모 : f1, f2 (공통되는 기능을 부모 class는 가지고 있음)
# 부모 -> 자식 (상속을 통해 공통되는 기능을 부모 class에서 가져옴)
# 자식 : (f1, f2) f3
# 1:f1 f2 f3      #
# 2:f1 f2    f4   #
# 3:f1 f2 f3 f4   #
# 4:f1 f2      f5 #

#메소드 오버라이딩
#부모클래스에서 정의되어있는 메소드를 자식클래스에서 새로 정의하여 사용

#객체1: f1 f2 f3
#객체2: f1 f2-2

class Cat:
    def __init__(self):
        self.sleepy = True
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def snack(self): # snack method의 새로운 정의
        print("muuu")

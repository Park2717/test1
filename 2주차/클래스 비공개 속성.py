class Cat:
    def __init__(self):
        self.sleepy = True
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def setAge(self, Age):
        self.__age = Age # __ 로 비공개 설정
        print("Set age to {}.".format(Age))
    def showAge(self):
        print("{0} years old.".format(self.__age))
        # 같은 class 안에 method만이 비공개 속성을 data를 사용할 수 있음
    def snack(self): # 수정됨
        print('eyaa~')

minyong = KoShort()
minyong.setAge(7) # self.age = 7로 초기화됨
minyong.snack()
minyong.showAge()
print(minyong.__age) #외부에서 접근 불가능

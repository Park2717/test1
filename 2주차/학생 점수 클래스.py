# Student 클래스
class Student:
    def __init__(self, korean, english, math):
        self.__korean = korean
        self.__english = english
        self.__math = math
        self.Everage = 0
    def showKorean(self):
        print("Korean:", self.__korean)
    def showEnglish(self):
        print("English:", self.__english)
    def showMath(self):
        print("Math:", self.__math)
    def showEverage(self):
        self.Everage = (self.__korean + self.__english + self.__math)/3
        print("Everage:",self.Everage)

HunTae = Student(korean = 80, english = 90, math = 70)
HunTae.showKorean()
HunTae.showEnglish()
HunTae.showMath()
HunTae.showEverage()

# 국적 클래스 만들기

print('-'*30)
d_persons = {'Guillaume':'Canada', 'Niklas':'Germany','Mark':'USA', 'Alex':'Swiss','Alberto':'Italia'}

class Person():
    nation = 'a Nation' # nation을 a Nation으로 초기화
    name = 'username' # name을 username으로 초기화
    def setName(self, target): # 이름을 직접 지정
        self.name = target
    def findNation(self, d_dict): # dict를 받아서 이름을 찾은 후 value값 찾음
        self.nation = d_dict[self.name]
    def setName(self):
        print(self.name)
        #print(self.name, end = ' ')
    def showNation(self):
        print(self.nation, end = '\n')
        #print(self.nation, end = ' ')


# 특정 class 함수로만 class 변수를 사용 가능
# 정해진 연산만 할 수 있기 때문에 에러율이 낮음

def add(a, b):
    return a+b

add(3, 7)
add('3', '7')

l_p = []
for i in range(len(d_persons)):
    l_p.append(Person())
    l_p[i].setName(list(d_persons.keys())[i])
    l_p[i].findNation(d_persons)
for i in range(len(d_persons)):
    l_p[i].showName()
    l_p[i].showNation()
    print()

## pN에 같은 class 지정
#p1 = Person()
#p2 = Person()
#p3 = Person()
#p4 = Person()
#p5 = Person()
## pN에 이름 지정해주기
#p1.setName(list(d_persons.keys())[0])
#p2.setName(list(d_persons.keys())[1])
#p3.setName(list(d_persons.keys())[2])
#p4.setName(list(d_persons.keys())[3])
#p5.setName(list(d_persons.keys())[4])
## pN에 부여된 이름 출력
#p1.showName() #p1.name을 출력
#p2.showName()
#p3.showName()
#p4.showName()
#p5.showName()
## pN에 self.name으로 국가를 찾아서 출력
#p1.findNation(d_persons)
#p2.findNation(d_persons)
#p3.findNation(d_persons)
#p4.findNation(d_persons)
#p5.findNation(d_persons)

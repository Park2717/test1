### 프로그래밍 과제 1
##2 자신의 이름 출력 프로그램
def Hello(name):
    print("hello my name is", name)
Hello('Park')
print()

##3 염기 구분 함수
def Nitro(what):
    d = {'A':'Adenine', 'T':'Thymine', 'C':'Cytosine', 'G':'Guanine', 'U':'Uracil'}
    print(d[what])
Nitro('A')
Nitro('T')
Nitro('G')
Nitro('C')
Nitro('U')
print()

##4 10/n 결과 출력
def divide(n):
    try:
        print(10/n)
    except ZeroDivisionError:
        print("Do not use Zero")

divide(5)
divide(0)
print()

##5 재귀 알고리즘을 사용하여 5! 구하기
def test(num):
    result = 1
    for i in range(num, 0, -1):
        result *= i
        if i == 1:
            print(result)
test(5)
print()

### 프로그래밍 과제 2

##1 파일을 파싱할 때 고려해야할 사항
# 파일을 less로 열어보고 어떤 형태인지 파악한 후
# 파일의 형태에 맞게 읽기 명령을 사용하여 파싱한다

##2 csv, tsv 파일의 차이점
# csv는 comma(,)로 자료를 구분한 것
# tsv는 tab키로 자료를 구분한 것

##3 json 파일은 무엇인가?
# JavaScript Object Notation의 약자
# 구조화된 데이터를 표현하고
# key : value와 같은 dictionary의 자료 형태를 가지고 있다.

##4 csv파일 json 파일을 바꾸어 보기

import json
class mkjson:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.ret = []
    def read_csv(self) -> list:
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if line.startswith("s"):
                    header = line.strip().split(",")
                    continue
                splitted = line.strip().split(",")
                self.ret.append(dict(zip(header, splitted)))
            print(self.ret)
    def make_json(self, l: list) -> None:
        with open("read_test.json", 'w') as handle:
            json.dump(l, handle, indent = 4)

j = mkjson("read_test.csv")
j.read_csv()
j.make_json(j.ret)
print(j.file_name)

def read_json(file_name: str) -> list:
    with open(file_name, 'r') as handle:
        l = json.load(handle)
    return l

l = read_json("read_test.json")
print(l)
print()

##5 k-mer 프로그램 (아직 못품)

DNA = ['A', 'T', 'G', 'C']
def k_mer(num):
    result = []
    count = num
    odd = []

# linux 환경에서 pip install biopython 설치
# import Bio
# Bio.__version__

#1 출력
print("Hello Bioinformatics")
print('-'*20)

#2 반지름 r인 원의 넓이
r = 4
PI = 3.14

area = (r**2) * PI
print(area)
print('-'*20)

#3 num1과 num2의 연산
num1 = 3
num2 = 5

print(num1 + num2)
print(num2 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1**2, '/', num2**2)
print('-'*20)

#4 3은 짝수인가 홀수인가
num1 = 3

if num1 % 2 == 1 :
    print("True")
else:
    print("False")
print('-'*20)

#5 21은 3의 배수인가 7의 배수인가
num1 = 21

if num1 % 3 == 0 and num1 % 7 == 0:
    print("3, 7 family")
elif num % 3 == 0:
    print("3 family")
elif num1 % 7 == 0:
    print("7 family")
else:
    print("no")
print('-'*20)


#6 1~10까지의 합
sum = 0
for i in range(1, 11, 1):
    sum += i
print(sum)
print('-'*20)

#7 짝수단만 출력
for i in range(2, 9, 2):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j)
print('-'*20)

#7-1 짝수배수만 구하기
def twice(num):
    for i in range(2, 9, 2):
        print(f"{i} x {j} = {i*j}")
        #파이썬 3에서부터 가능
twice(3)
print('-'*20)

#8 while을 사용해서 5!를 구하라
num = 5
result = 1

while num > 0:
    result *= num
    num -= 1
print(result)
print('-'*20)

#9 함수 greet 만들고 함수 호출시 "Hello, Bioinformatics" 출력
def greet() -> None: #return이 없을 때 None 쓰기 (반환되는게 없다는 것을 보여줄 때 사용)
    print("Hello, Bioinformatics")
greet()
print('-'*20)

#10 mySum 함수 생성 (매개인자 2개 서로 더하기)
def mySum(num1, num2):
    print(f"{num1} + {num2} = {num1+num2}")
mySum(2, 3)
mySum(5, 7)
mySum(10, 15)
print('-'*20)

# 10-1
def mySum(num1: int, num2: int)->int:
    return num1 + num2

res1 = mySum(2, 3)
res2 = mySum(5, 7)
res3 = mySum(10, 15)
print(res1)
print(res2)
print(res3)
print('-'*20)

#11, 12 5! 계산 프로그램
def fac(num):
    if num > 0 :
        result = 1
        for i in range(num, 0, -1):
            result *= i
        print(result)
    else:
        print("No")
fac(5)
print('-'*20)

#13 사용자로부터 값 받기
#name = input("your name:")
#print(f"Hello {name}")

#14 숫자? 문자?
#word = 1
#if word.isdigit():
#    print("int")
#elif word.isalpha():
#    print("str")
#else:
#    print("None")

#15 커맨드라인에서 인수 입력받기 (리눅스 환경 필요)
#import sys

#print(f"cmd_pic_generate {sys.argv[1]}")
#print(f"run -> sample{sys.argv[1]}")

# 리눅스에서 for문
#for i in 1 2 3:
#do
#    python 015.py ${i} #달러를 사용 중괄호는 안써도 되지만 범위 잡아주는데 좋음
#done

#print('-'*20)

#16 파일 읽기

#f = open("read_sample.txt",'r')
#r = f.readlines()
#f.close()

#for s in r:
#    print(s.strip())

with open("read_sample.txt", 'r') as handle:
    for line in handle:
        if line.startswith(">"): #header 날리기
            continue
        print(line.strip()) #enter가 있는데 strip으로 인해 없애줌
print('-'*20)

#import sys
#f = sys.argv[1]
#with open(f, 'r') as handle: <- 가능

#16-1 covid19 seq 다운받아서 counting 하기

d = {}
with open("sequence.fasta", 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d :
                d[s] += 1
            else:
                d[s] = 1
print(d)
total = 0
for k, v in d.items():
    total += v
print(total)
print('-'*20)

#17 파일 쓰기
with open("seqcount.txt", 'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")

with open("seqcount.txt", 'r') as handle:
    for line in handle:
        print(line.strip())
print('-'*20)

## sys.argv[1]이 없을 때
# if len(sys.argv) != 2:
#    print(f"#usage: python {sys.argv[0]} [name]")
#    sys.exit()

#try :
#    with open(f, 'r') as handle:
#        read = handle.readlines() # list로 변환
#except FileNotFoundError:
#    print(f"{f} not found.. please check..")
#    sys.exit()
#print(read)

#try:
#    num = int(sys.argv[1])
#    print(10 / num)
#except ZeroDivisionError:
#    print("Do not use Zero")
#    sys.exit()
#except ValueError:
#    print("input not valid")
#    sys.exit()
## python read.py 0

#20 문자열 더하기
s1 = "Bio"
s2 = "Informatics"
s = s1 + s2
print(s)
print('-'*20)

#21
Seq1 = 'AGTTTATAG'
print(Seq1[3:6])
print('-'*20)

#22
Seq1 = 'ATGttATaG'
print(Seq1.upper())
print('-'*20)

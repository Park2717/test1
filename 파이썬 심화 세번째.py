class C:
    def __init__(self):
        print("class C's instance")
        self.name = 'ccc'
        self.age = 0
    def say_hi(self):
        print("hi")
    def add_age(self, n:int):
        self.age += n
    def __str__(self): #그냥 c만 출력했을때
        return "__str__ call"
    def __repr__(self): # c만 입력했을때(인터프리터 환경에서)
        return "__repr__ call"
    def __abs__(self): # abs 함수 추출
        print("__abs__ call")
    def __len__(self): # len 함수 추출
        print("__len__ call")
    def __add__(self, other):
        return self.age + other
'''
c = C() #class C's instance
print(c) # __str__ call
print(c.name) #ccc
c.say_hi()
print(c.age) #0
c.add_age(7)
print(c.age) #7
print(abs(10))
print(abs(-10))
print(abs(c)) # __abs__ call, None
print(c.__add__(2)) #9
'''
#'''
import Bio
from Bio import SeqIO

record = SeqIO.read("read_fasta.txt", "fasta")
A = record.seq.count("A")
C = record.seq.count("C")
G = record.seq.count("G")
T = record.seq.count("T")

print(f"A: {A}") # A: 497
print(f"C: {C}") # C: 444
print(f"G: {G}") # G: 585
print(f"T: {T}") # T: 514
#'''


import collections
class FASTQ:
    DNA_d = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    def __init__(self, file_name):
        self.file_name = file_name
        self.read_num = 0
        self.DNA = []
    def count_read_num(self):
        cnt = 0
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if cnt % 4 == 0:
                    header = line.strip()
                    self.read_num += 1
                elif cnt % 4 == 1:
                    seq = line.strip()
                    self.DNA += line.strip()
                     #for s in seq:
                    #     if s in self.base:
                    #         self.base[s] += 1
                    #     else:
                    #         self.base[s] = 1
                elif cnt % 4 == 3:
                    qual = line.strip()
                cnt += 1
            print(collections.Counter(self.DNA))
            print(sum(collections.Counter(self.DNA).values()))
f = FASTQ("read_fasta2.txt")
f.count_read_num()

def pibo(num):
    result = []
    for i in range(0, num):
        if i < 2 :
            result += [i]
        else:
            result += [result[i-1] + result[i-2]]
    print(result)
pibo(13)

#'''
#import sys

def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n-1)+fib(n-2) #재귀 함수

#n = int(sys.argv[1])
#print(fib(n))
print(fib(9))

l1 = ['A', 'T', 'G', 'C']
l2 = ['A', 'T', 'G', 'C']
def k_mer(l1, l2, num):
    if num == 1:
        return l2
    l_tmp = []
    for i in l1:
        for j in l2:
            l_tmp.append(i+j)
    return k_mer(l1, l_tmp, num-1)
print(k_mer(l1, l2, 3))

# 리눅스 환경에서 압축하기
# gzip covid19.fataq
# zless covid19.fasta.gz <- 디렉터리 파일을 볼 수 있게함
# -S 옵션 추가로 끊김없이 계속 출력된 것을 볼 수 있다.
# 압축 풀기
# gunzip covid19.fasta.gz
# 압축 풀고 압출 파일 남기기
# gzip -c covid19.fasta > covid19.fasta.gz

#import sys
#import gzip

#if len(sys.argv) != 2:
#    print(f"#usage: python {sys.argv[0]} [fasta.gz]")
#    sys.exit()

#f = sys.argv[1]

#with gzip.open(f, 'rb') as handle: #open 대신 gzip.open을 사용, r대신 rb를 사용 read binary
#    for line in handle:
#        line = line.decode("utf-8") #utf-8이라는 것으로 decoding하여 bite를 str로 전환
#        print(type(line.strip())) #type을 써서 앞줄이 어떤 자료인지 확인
#        sys.exit() # 너무길어서 한줄만 출력

# python 016-1.py covid19.fasta.gz

# 연습
#import sys
#import gzip

#if len(sys.argv) != 2:
#    print(f"#usage: python {sys.argv[0]} [fasta.gz]")
#    sys.exit()

#f = sys.argv[1]
#d = {}

#with gzip.open(f, 'rb') as handle:
#    for line in handle:
#        line = line.decode("utf-8").strip() #strip도 같이 시킴
#        if line.startswith(">"): # 첫번째줄 제거
#            continue
#        print(line.strip())
#        for i in line.strip():
#            if i in d :
#                d[i] += 1
#            else:
#                d[i] = 1

#with open("result1.txt", 'w') as handle:
#    handle.write(f"A: {d['A']}\n")
#    handle.write(f"C: {d['C']}\n")
#    handle.write(f"G: {d['G']}\n")
#    handle.write(f"T: {d['T']}\n")

#26
seq1 = 'ATGTTATAG'
print(seq1)
print('-'*20)
for i in range(0, len(seq1),3):
    print(seq1[i:i+3])
print('-'*20)

#27
print(seq1[::-1])
print('-'*20)

#28
d = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }

trans = ''
for i in range(len(seq1)):
    trans += (d[seq1[i]])
print(seq1)
print(trans)
print('-'*20)

#28-1 리눅스에서 열기
#def comp1(seq:str) -> str:
#    comp = ""
#    for s in seq:
#        if s == "A":
#            comp += "T"
#        elif s == "C":
#            comp += "G"
#        elif s == "G":
#            comp += "C"
#        elif s == "T":
#            comp += "A"
#    return comp

## p028.py
#def comp2(seq: str) -> str:
#    d = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }
#    comp = ""
#    for s in seq:
#        comp+=d_comp[s]
#    return comp

#if __name__ == "__main__":
##다른 python file에서 짜놓은 함수를 사용가능한데
##이렇게 해놓으면 import로 불러와도 이쪽은 사용 불가
#    if len(sys.argv) != 2:
#        print(f"#usage: python {sys.argv[0]} [string]")
#        sys.exit()

#    seq = sys.argv[1] #ATGTTATAG
#    c1 = comp1(seq)
#    c2 = comp2(seq)
#    print(c1)
#    print(c2)

## 인터프리터 환경
#import p028
#p028.comp1(seq)

#29
print('C' in seq1)
print('-'*20)

#30
seq1 = 'AGTTTATAG'
for i in range(len(seq1)):
    if seq1[i:i+2] == 'TT':
        print(i,seq1[i:i+2])
print('-'*20)
# seq1.index("TT")는 첫번째 TT를 읽고 난 후에 읽은 것 다음으로 넘어가 버린다
# 즉 2번째 위치만 출력이 된다.

#31~33
seq = 'AA,AC,AG,AT'
seq1 = seq.split(',')
print(seq1)
print('-'*20)
seq1.append('CA')
print(seq1)
print('-'*20)
print(seq1[::-1])
print('-'*20)

#34
list = [3, 1, 1, 2, 0, 0, 2, 3, 3]
print(max(list))
print(min(list))
print('-'*20)

#35
import collections
print(collections.Counter(list))
print('-'*20)

d = {}
for i in list:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
print('-'*20)

# set()의 type은 seq이다.
# set는 append 대신 add를 사용한다

##프로그래밍 과제 1
#2 자신의 이름 출력 프로그램
#def hello():
#    print(f"Hello! my name is {name}")
#hello(park)

# txt 파일 읽기
ret = ""
with open('read_sample.txt','r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        else:
            ret += line.strip()
    print(ret)
print('-'*20)

#def readtxt(file_name: str) -> str:
#    ret : ""
#    with open(file_name, 'r') as handle:
#        for line in handle:
#            if line.startswith(">"):
#                continue
#            else:
#                ret += line.strip()
#    return ret

ret = []
with open('read_sample.tsv', 'r') as handle:
    for line in handle:
        if line.startswith("#"):
            header = line.strip().split("\t")
            continue
        splitted = line.strip().split("\t")
        ret.append(dict(zip(header, splitted)))
    print(ret)

print('-'*20)

#zip 원리
l1 = ["A", "B", "C"]
l2 = [1, 2, 3]
zip(l1, l2)
print(dict(zip(l1, l2))) #{'A':1, 'B':2, 'C':3}
print('-'*20)

# :%s/,/^I/g  vim에서 ,를 tab키로 바꾸기
# ^I는 탭 문자
# set list vim에서 스페이스바와 tab키 구분하기 위해 문자로 보여줌
# set nolist 하면 다시 원래되로 보임

#def read_csv(file_name: str) -> list:
ret = []
with open('read_sample.csv','r') as handle:
    for line in handle:
        if line.startswith("#"):
            header = line.strip().split(",")
            continue
        splitted = line.strip().split(",")
        d = dict(zip(header, splitted))
        ret.append(d)
    print(ret)
#    return ret

# json 파일 만들기
import json
def to_json(l: list) -> None:
    with open("read_sample.json",'w') as handle:
        json.dump(l, handle, indent = 4)
to_json(ret)

print('-'*20)

# json 읽기
def read_json(file_name: str) -> list:
    with open(file_name, 'r') as handle:
        l = json.load(handle)
    return l

l = read_json("read_sample.json")
print('json file:', l)
print('-'*20)

# k-mer 만들기

# GATK Best Practice Pipeline

class FASTA:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.count = {}
        self.length = 0
        self.rcount = 0

    def count_base(self):
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if line.startswith(">"):
                    continue
                line = line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1
    def get_length(self):
        for k, v in self.count.items():
            self.length +=v

    def read_count(self):
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if line.startswith("@"):
                    self.rcount += 1
                    continue

#    def __len__(self):
#        self.get_length()
#        return self.length

## linux 환경에서
#if __name__ == "__main__":
#    if len(sys.argv) !=2:
#        print(f"#usage: python {sys.argv[0]} [fasta]")
#        sys.exit()
#    file_name = sys.argv[1]
#    t = FASTA(file_name)
#    t.count_base()
#    t.get_length()
#    print(t.count)
#    print(t.length)

f = FASTA("read_fasta.txt")
f.count_base()
f.get_length()
print(f.count)
print(f.length)
#print(len(f))
print('-'*20)

f = FASTA("read_fasta2.txt")
f.read_count()
print(f.rcount)

print('-'*20)

class FASTQ:
    def __init__(self, file_name):
        self.file_name = file_name
        self.read_num = 0
    def count_read_num(self):
        cnt = 0
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if cnt % 4 == 0:
                    header = line.strip()
                    self.read_num += 1
                elif cnt % 4 == 1:
                    seq = line.strip()
                elif cnt % 4 == 3:
                    qual = line.strip()
                cnt += 1

f = FASTQ("read_fasta2.txt")
f.count_read_num()
print(f.read_num)

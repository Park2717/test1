#1
def read_fasta(file_name):
    d = {}
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            for s in line:
                if s == "\n":
                    continue
                elif s in d:
                    d[s] += 1
                else:
                    d[s] = 1
    return d
print(read_fasta("read_fasta.txt"))
f = read_fasta("read_fasta.txt")
#2
import json
def mkjson(l: list) -> None:
    with open("test.jason", 'w') as handle:
        json.dump(l, handle, indent = 4)

def rdjson(file_name: str)-> str:
    with open(file_name, 'r') as handle:
        l = json.load(handle)
    return l

mkjson(f)
print(rdjson("test.jason"))
'''
#3
def rev_line(file_name):
    d = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rev_fasta = ''
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            for s in line.strip():
                rev_fasta += d[s]
    print(rev_fasta[::-1])
rev_line("read_fasta.txt")
'''
#4
print()
record_name = []
result = []
n = 0
v = 0
with open("sample.fasta",'r') as handle:
    for line in handle:
        if line.startswith(">"):
            record_name += [line.replace('>','').replace("\n",'')]
            if n != 0:
                result += [d]
                n = 0
                v += 1
            d = {}
            continue
        for s in line:
            if s == "\n":
                continue
            elif s in d:
                d[s] += 1
            else:
                d[s] = 1
        n = 1
    result += [d]
    for i in range(len(record_name)):
        print(record_name[i], result[i])

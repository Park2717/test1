#! /usr/bin/python

total = 0

with open("077.bed", 'r') as handle:
    for line in handle:
        splitted = line.strip().split("\t")
        start = int(splitted[1])
        end = int(splitted[2])
        total += end - start

print(total)

count = 0
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        count += 1
print(count)

cnt = 0
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        else:
            splitted = line.strip().split("\t")
            if splitted[6] == 'PASS':
                cnt += 1
print(cnt)


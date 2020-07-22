#! /usr/bin/python

total = 0

with open("077.bed", 'r') as handle:
    for line in handle:
        splitted = line.strip().split("\t")
        start = int(splitted[1])
        end = int(splitted[2])
        total += end - start

print(total)

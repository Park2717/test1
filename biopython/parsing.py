#! /usr/bin/python

#from Bio import SeqIO
#for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
#    print(seq_record.id)
#    print(repr(seq_record.seq))
#    print(len(seq_record))

from Bio import SeqIO
for seq_record in SeqIO.parse("read.fastq", "fastq"):
    print(seq_record.id)


# 앞으로 읽어도 거꾸로 읽어도 sequence가 같은 서열

# 5  3
# GATC
# CTAG
# 3  5

#seq = input('input seq.: ')

seq = 'AAATTTT'
rev_seq = seq[::-1]
print(rev_seq)

#for i in range(len(seq)):
#    rev_seq += seq[-(i+1)]
#print(rev_seq)

rev_seqcom = ''
com = {'A':'T', 'T':'A','G':'C','C':'G'}
for i in range(len(rev_seq)):
    rev_seqcom += com[rev_seq[i]]
print(rev_seqcom)

if rev_seqcom == seq:
    print(seq, "is panlidromic.")
else:
    print(seq, "is not panlidromic.")

# 정답안

llll_palindromic = 0

if len(seq)%2 == 1:
    print("Diff.")
else:
    for i in range(len(seq)):
        if seq[i] == com[seq[-(i+1)]]:
            llll_palindromic += 0
        else:
            llll_palindromic += 1
if llll_palindromic == 0:
    print('{0} is palindromic.'.format(seq))
else:
    print('{0} base differ.'.format(i_palindromic))

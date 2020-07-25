#   5                 3
s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'
#   3                 5

d_dna = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

def point(sam1, sam2):
    if len(sam1) == len(sam2):
        point_cnt = 0
        sam1_list = []
        sam2_list = []
        for i in range(len(sam1)):
            sam1_list.append(sam1[i])
            sam2_list.append(sam2[i])
        for k in range(len(sam1_list)):
            if sam1_list[k] != sam2_list[k]:
                point_cnt += 1
    print(point_cnt)

point(s, t)

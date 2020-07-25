# 점수를 입력받아 학점을 출력하세요

rank = int(input("write rank:"))
rank = 95

if rank >= 90 :
    print("A")
else:
    if rank >=80 :
        print("B")
    else:
        if rank >=70 :
            print("C")
        else:
            if rank >=60 :
                print("D")
            else:
                print("F")
print("is your rank")

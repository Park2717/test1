# a, b 입력을 받아서 -> a부터 b 사이에 있는 홀수를 다 더해서 출력하라

# 정답안

fir = int(input("first :"))
sec = int(input("second :"))

# 100 ~ 200
#range(100)  0 ~ 99
#range(201)  0 ~ 200

result = 0
l_odd = []
fir = 100
sec = 200

for i in range(fir, sec + 1):
    print(i, end = ' ')
    if i % 2 == 1 :
        l_odd.append(i)
        result +=i

result = sum(l_odd)
print(result)

# 내가한거

a = 100
b = 200
list = []
while True :
    if a < b :
        for i in range(a, b):
            start = a
            a += 1
            if divmod(a,2)[1]==0:
                continue
            elif divmod(a,2)[1]==1:
                if a >= b:
                    break
                else:
                    list.append(a)
    elif a > b :
        for i in range(a, b):
            start = b
            b +=1
            if divmod(a,2)[1]==0:
                continue
            elif divmod(a,2)[1]==1:
                if b >= a:
                    break
                else:
                    list.append(b)
print(sum(list))

result = 0

# 희재한거

while(1) :
    val = input("Enter the number 2 numbers : ")

    # split
    num1, num2 - val.split(" ")

    # check whether inputs are numbers
    if num1.isdigit() and num2.isdigit() :

        # convert num1 and num2 into numbers
        num1 = int(num1)
        num2 = int(num2)

        # check whether a < b
        if num1 > num2 :
            print("Start number is bigger than end number!")
            continue
        else:
            for i in range(num1, num2) :
                if i % 2 == 1 :
                    result += i
        break
    else:
        print("Wrong Input! (Enter Numbers)")
        continue
print(result)

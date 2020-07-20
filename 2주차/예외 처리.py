def calc(i1, i2):
    return i1+i2

Num1 = input('Num1:')
Num2 = input('Num2:')

try:
    Num1 = int(Num1)
except ValueError:
    print("Exception")

print("Num1", type(Num1))
print("Num2", type(Num2))

#result = calc(Num1, Num2)

#try:
#    Num1 = int(Num1)
#except ValueError:
#    print("ValueError")

Num1 = input('Give age:')

if not Num1.isdigit():
    raise pleaseGiveString

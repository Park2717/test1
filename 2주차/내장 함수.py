cnt = 0
l_list = [1,2,3,4]

for i in l_list: # for문으로 l_list 구성원소 더하기
    cnt += i
print(cnt)

print(sum(l_list)) # 내장 함수 sum으로 더하기
print('-'*10)

all ([True, 1, 0])

any([True, 1, 0])

dir('apple') # apple. 으로 시작해서 사용할 수 있는 명령어 보여줌

'apple'.endswith('le') # apple이 le로 끝나는 것이 맞는가? True
'apple'.startswith('a') # apple이 a로 시작하는 것이 맞는가? True
# '> apple addInfor'.startswith('>') True
# not '# sfdgh'.startswith('#')

# 7//3 몫은 2 7%3 나머지는 1
divmod(7,3) # (2, 1) 튜플로 나옴 <- 인덱싱 가능 divmod(7,3)[0]

l_list = ['apple', 'banana']
for a, b in enumerate(l_list) : # 출력값 앞에 인덱스 번호를 부착하여 출력함
    print(a, b)     # 0 apple 1 banana
    print('a:', a)  # a: 0     a: 1
    print('b:', b)  # b: apple b: banana

eval('5+7') # 계산
# eval('p = 5') 변수에는 안들어감
p = eval('5+7') # 이거는 됨

len([1, 2, 3]) # 길이를 구함
len([1, 2, 3, '3456'])
len('apple') # 5

l_list = ['apple', 'banana']
s_str = 'abcd'

for i in s_str :
    print(i)

print(len(l_list)) # 2
print(len(s_str)) # 4

list({3, 4}) #[3, 4]

max(list(range(5))) # 4
min(list(range(5))) # 0

sorted(list(range(5))) # [0, 1, 2, 3, 4] 작은순서대로 정렬, 원래 list는 변하지 않음

type(l_list) # <class 'list'> 타입 알려줌

# 연습문제 1 생일-일자 나타내기

d_reg = {'regNum0':'951213-0000000', 'regNum1': '960125-0000000', 'regNum2':'970705-0000000'}
d_month = {1:'Jan',2:'Feb', 3:'Wen', 4:'Apr', 5:'May', 6:'Jun', 7:'July', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
d_month_str = {'01':'Jan','02':'Feb', '03':'Wen', '04':'Apr', '05':'May', '06':'Jun', '07':'July', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}

a = int(d_reg['regNum0'][2:4])
a_str = d_reg['regNum0'][2:4]
ad = d_reg['regNum0'][4:6]
b = int(d_reg['regNum1'][2:4])
b_str = d_reg['regNum1'][2:4]
bd = d_reg['regNum1'][4:6]
c = int(d_reg['regNum2'][2:4])
c_str = d_reg['regNum2'][2:4]
cd = d_reg['regNum2'][4:6]

# d_month를 이용한 답
print(d_month[a]+'-'+ad)
print(d_month[b]+'-'+bd)
print(d_month[c]+'-'+cd)

# d_month_str를 이용한 답
print(d_month_str[a_str]+'-'+ad)
print(d_month_str[b_str]+'-'+bd)
print(d_month_str[c_str]+'-'+cd)

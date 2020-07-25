

calc = '10 USD, 5 EUR, 7 YPY, 9 CNY'
print(calc)

d_ratio = {'USD' : '1,203.82', 'EUR':'1,354.73','YPY':'11.22','CNY':'172.04'}

for i in range(0,4) :
    a = calc.replace(' ','').split(',')[i][-3:] ## unit list
    b = float(d_ratio[a].replace(',','')) ##dic_ratio
    c = int(calc.split(',')[i][0:2]) ##how_much
    d = b * c ## calculate
    print(round(d, 2),"KBW", end = " ")

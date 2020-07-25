
calc = '10 USD, 5 EUR, 7 YPY, 9 CNY'
print(calc)

d_ratio = {'USD' : '1,203.82', 'EUR':'1,354.73','YPY':'11.22','CNY':'172.04'}

calc_ls = calc.split(", ")
print(calc_ls)

usd_ls = calc_ls[0].split(" ")
eur_ls = calc_ls[1].split(" ")
ypy_ls = calc_ls[2].split(" ")
cny_ls = calc_ls[3].split(" ")

usd = int(usd_ls[0]) * float(d_ratio[usd_ls[1]].replace(",", ""))
eur = int(usd_ls[0]) * float(d_ratio[eur_ls[1]].replace(",", ""))
ypy = int(usd_ls[0]) * float(d_ratio[ypy_ls[1]].replace(",", ""))
cny = int(usd_ls[0]) * float(d_ratio[cny_ls[1]].replace(",", ""))
print("{0} KRW, {1} KRW, {2} KRW, {3} KRW".format(round(usd, 2), eur, ypy, round(cny,2)))
print()

cnt = []
cnt +='*'
print(cnt)
cnt +='*'
print(cnt)
print(cnt.count('*'))

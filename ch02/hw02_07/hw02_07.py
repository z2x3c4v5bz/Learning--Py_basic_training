# hw02_07
money = int(input('請輸入存款金額：(整數)'))
print('')
yrate = float(input('請輸入年利率：(浮點數)')) # 書上有錯，這裡要填0.1，而不是10
print('')
y = int(input('請輸入存款年數：(整數)'))
print('單利：%d元%d年的本利和=%12.1f' % (money, y, money + money * yrate * y))
print('複利：%d元%d年的本利和=%12.1f' % (money, y, money * ((1 + yrate) ** y)))
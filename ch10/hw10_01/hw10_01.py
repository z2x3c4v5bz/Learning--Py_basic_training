# hw10_01
while True:
    try:
        dividend = int(input('輸入被除數 : '))
    except ValueError:
        print('輸入錯誤,請輸入整數')
        continue
    break
while True:
    try:
        divisor = int(input('輸入除數 : '))
    except ValueError:
        print('輸入錯誤,請輸入整數')
        continue
    if divisor == 0:
        print('除數為0,請重新輸入')
        continue
    print('{0} / {1} = {2}'.format(dividend, divisor, dividend / divisor))
    break
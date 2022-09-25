# hw10_01


if __name__ == '__main__':

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


''' Output

輸入被除數 : 2.4
輸入錯誤,請輸入整數
輸入被除數 : 24
輸入除數 : 0
除數為0,請重新輸入
輸入除數 : 5
24 / 5 = 4.8

'''

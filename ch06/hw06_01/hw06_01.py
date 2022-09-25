# hw06_01


def gcd(a, b):
    while a % b:
        a, b = b % a, a
    return a + b


if __name__ == '__main__':

    usera = int(input('輸入第一個正整數a : '))
    userb = int(input('輸入第二個正整數b : '))

    print('a, b兩整數的GCD為%d' % gcd(usera, userb))


''' Output

輸入第一個正整數a : 30
輸入第二個正整數b : 17
a, b兩整數的GCD為1

'''

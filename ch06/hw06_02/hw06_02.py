# hw06_02


def comrate(principal, arate, year):

    #本利和 = 本金 * (1 + 月利率) ^ 期數
    
    return principal * ((1 + arate / 100 / 12) ** (12 * year))


if __name__ == '__main__':

    print('==複利率本利和試算==')

    p = eval(input('請輸入本金 : '))
    a = eval(input('請輸入年利率(%) : '))
    y = eval(input('幾年後領回 : '))

    print('***%d年後領回本利和 : %d' % (y, round(comrate(p, a, y))))


''' Output

==複利率本利和試算==
請輸入本金 : 30000
請輸入年利率(%) : 0.5
幾年後領回 : 3
***3年後領回本利和 : 30453

'''

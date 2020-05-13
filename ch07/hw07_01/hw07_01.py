# hw07_01
def myfun(n):
    if n == 1:
        print('1 = ', end='')
        return 1
    else:
        print('%d + ' % (n ** 2), end='')
        return n ** 2 + myfun(n - 1)

while True:
    usern = eval(input('n = '))
    if usern > 0 and usern <= 10:
        break
    else:
        print('Error!')

print('%d' % myfun(usern))


'''

n = 5
25 + 16 + 9 + 4 + 1 = 55

'''

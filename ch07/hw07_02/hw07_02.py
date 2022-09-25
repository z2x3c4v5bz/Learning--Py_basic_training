# hw07_02


def myfun(n):

    if n == 1:

        return 0

    else:

        return (n * (n - 1)) + myfun(n - 1)


if __name__ == '__main__':

    while True:

        usern = eval(input('n = '))

        if usern >= 2 and usern <= 10:

            break

        else:

            print('Error!')

    for i in range(1, usern + 1):

        if i != usern:

            print('%d +' % (i * (i + 1)), end=' ')

        else:

            print('%d' % (i * (i + 1)), end=' = ')

    print('%d' % myfun(usern + 1))


''' Output

n = 5
2 + 6 + 12 + 20 + 30 = 70

'''

# hw07_03


def ap(a, d, n):

    if n == 1:

        return a

    else:

        return a + ap(a + d, d, n - 1)


if __name__ == '__main__':

    firstTerm = eval(input('First term (a) = '))
    commonDifference = eval(input('Common difference (d) = '))
    numberOfTerms = eval(input('Number of terms (n) = '))

    print('The sum of the arithmetic progression is %d.' % ap(firstTerm, commonDifference, numberOfTerms))


''' Output

First term (a) = 1
Common difference (d) = 2
Number of terms (n) = 10
The sum of the arithmetic progression is 100.

'''

# hw06_04
def searchprime(N):
    for num in range(2, N):
        n = 2
        isprime = True
        while n <= (num ** (0.5)):
            if not (num % n):
                isprime = False
                break
            n += 1
        if isprime:
            print(num, end = ' ')

N = eval(input('求質數，請輸入一個數 : '))
print('1 ~ %d 的質數如下 : ' % (N))
searchprime(N)


'''

求質數，請輸入一個數 : 100
1 ~ 100 的質數如下 :
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

'''

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

N = eval(input('求質數，請輸入一個質數 : '))
print('1 ~ %d 的質數如下 : ' % (N))
searchprime(N)
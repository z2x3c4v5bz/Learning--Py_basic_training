# hw07_04
def isprime(n_i):
    i = 2
    while i <= (n_i ** (0.5)):
        if not (n_i % i):
            return False
        i += 1
    return True

def searchprime(n_s):
    primes = []
    for i in range(2, n_s):
        if isprime(i):
            primes.append(i)
    return primes

def myfun(n):
    if isprime(n):
        print(n)
        return
    else:
        primes = searchprime(n)
        for i in primes:
            if not (n % i):
                print('%d * ' % i, end='')
                return myfun(n // i)

usern = eval(input('Give me a number : '))
print('%d = ' % usern, end='')
myfun(usern)
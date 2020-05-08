# hw05_01
num = [x for x in range(1,10)]

for i in num:
    for j in num:
        print("%2d" % (i * j), end = ' ')
    print('')
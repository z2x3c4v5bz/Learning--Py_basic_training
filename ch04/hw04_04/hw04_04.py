# hw04_04
i, j = 1, 1
while True:
    for y in range(j):
        print('%d*%d=%d' % (i, y + 1, i * (y + 1)), end='')
    print('')
    if i == 9:
        break
    else:
        i += 1
        j += 1
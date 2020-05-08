# hw05_04
arra = [[1, 2, 3], [4, 5, 6]]
arrb = [[1, 2], [3, 6], [4, 2]]
arr = []

print('矩陣 A')
for i in range(len(arra)):
    for j in range(len(arra[i])):
        print('%d ' % arra[i][j], end='')
    print('')

print('\n矩陣 B')
for i in range(len(arrb)):
    for j in range(len(arrb[i])):
        print('%d ' % arrb[i][j], end='')
    print('')

print('\n矩陣 A * 矩陣 B')
for i in range(len(arra)):
    for j in range(len(arrb[i])):
        x = 0
        for k in range(len(arra[i])):
            x += arra[i][k] * arrb[k][j]
        print('%d ' % x, end='')
    print('')
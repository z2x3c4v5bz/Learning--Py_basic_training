# hw05_03
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print('矩陣翻轉前:')
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print('%d ' % arr[i][j], end='')
    print('')
arr.reverse()

print('\n矩陣翻轉後:')
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print('%d ' % arr[i][j], end='')
    print('')
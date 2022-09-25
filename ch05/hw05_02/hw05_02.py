# hw05_02


if __name__ == '__main__':

    name = ['老張', '發叔', '李董', '豪哥', '小何']
    age = [54, 46, 50, 40, 38]

    user = int(input('1.由小到大排序  2.由大到小排序:'))

    for loop in range(1, 5):

        for index in range(0, (5 - loop)):

            if age[index] > age[index + 1] and user == 1:

                tempage = age[index]
                tempname = name[index]
                age[index] = age[index + 1]
                name[index] = name[index + 1]
                age[index + 1] = tempage
                name[index + 1] = tempname

            elif age[index] < age[index + 1] and user == 2:

                tempage = age[index + 1]
                tempname = name[index + 1]
                age[index + 1] = age[index]
                name[index + 1] = name[index]
                age[index] = tempage
                name[index] = tempname

    if user == 1:

        print('由小到大排序: ', end = '')

    else:

        print('由大到小排序: ', end = '')

    for i in range(5):
        print('%s:%d' % (name[i], age[i]), end=' ')
        
    print('')


''' Output

1.由小到大排序  2.由大到小排序:1
由小到大排序: 小何:38 豪哥:40 發叔:46 李董:50 老張:54

'''

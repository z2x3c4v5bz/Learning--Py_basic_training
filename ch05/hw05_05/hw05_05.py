# hw05_05


if __name__ == '__main__':

    Data = [['老張', '0911443300'], ['Mary', '0928000001'],
            ['發叔', '0431748484'], ['Tom', '0912345678'],
            ['李董', '0255111111'], ['豪哥', '0977229900'],
            ['小柯', '0928888888']]

    searchname = input('輸入查詢的姓名 : ')

    for i in range(len(Data)):

        if searchname == Data[i][0]:

            print('%s 的電話號碼為 %s' % (Data[i][0], Data[i][1]))

            break

    else:

        print('無 %s 的資料' % searchname)


''' Output

輸入查詢的姓名 : Mary
Mary 的電話號碼為 0928000001

'''

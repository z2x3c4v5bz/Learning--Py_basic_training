# hw09_01


if __name__ == '__main__':

    eng2zh = { 'apple':'蘋果',
            'break':'中斷',
            'continue':'繼續'}

    while True:

        user = int(input('=' * 23 + '\n1.新增/修改字典\n2.刪除單字\n3.單字查詢\n4.結束程式\n請輸入選項(1~4) : '))

        if user == 4:

            break

        elif user == 1:

            word_eng = input('請輸入單字 : ')

            if word_eng not in eng2zh:

                newword = input('新增 {0} 的中文 : '.format(word_eng))

            else:

                newword = input('修改 {0} 的中文 : '.format(word_eng))

            eng2zh[word_eng] = newword

        elif user == 2:

            word_eng = input('請輸入單字 : ')

            if word_eng not in eng2zh:

                print('不存在字典中')

            else:

                del eng2zh[word_eng]

        elif user == 3:

            word_eng = input('請輸入單字 : ')

            if word_eng not in eng2zh:

                print('不存在字典中')

            else:

                print('{0} 的中文是 {1}'.format(word_eng, eng2zh[word_eng]))

        else:

            continue


''' Output

=======================
1.新增/修改字典
2.刪除單字
3.單字查詢
4.結束程式
請輸入選項(1~4) : 3
請輸入單字 : apple
apple 的中文是 蘋果
=======================
1.新增/修改字典
2.刪除單字
3.單字查詢
4.結束程式
請輸入選項(1~4) : 4

'''

# hw02_03


if __name__ == '__main__':

    i1 = int(input('請輸入整數值：'))
    print('%d 的資料型別為 %s\n' % (i1, type(i1)))

    f1 = float(input('請輸入浮點數值：'))
    print('%9f 的資料型別為 %s\n' % (f1, type(f1)))

    b1 = bool(input('請輸入布林值：'))
    print('%s 的資料型別為 %s\n' % (b1, type(b1)))

    s1 = str(input('請輸入字串資料：'))
    print('%s 的資料型別為 %s' % (s1, type(s1)))


''' Output

請輸入整數值：5
5 的資料型別為 <class 'int'>

請輸入浮點數值：3.5
 3.500000 的資料型別為 <class 'float'>

請輸入布林值：True
True 的資料型別為 <class 'bool'>

請輸入字串資料：I love Python
I love Python 的資料型別為 <class 'str'>

'''

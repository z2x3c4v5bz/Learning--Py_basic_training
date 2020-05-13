# hw03_01
user = int(input('請輸入一個非零的整數：'))
print('所輸入的整數為', end=' ')
if user % 2 == 0:
    if user > 0:
        print('正偶數')
    else:
        print('負偶數')
else:
    if user > 0:
        print('正奇數')
    else:
        print('負奇數')


'''

請輸入一個非零的整數：66
所輸入的整數為 正偶數

'''

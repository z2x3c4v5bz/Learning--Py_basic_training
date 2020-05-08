# hw04_02
print('===主功能表===')
print('1.新增作業')
print('2.修改作業')
print('3.查詢作業')
print('0.結束程式')
while True:
    user = int(input('請輸入選項(0~3):'))
    if user == 0:
        print('結束程式！')
        break
    elif user == 1:
        print('新增作業...')
    elif user == 2:
        print('修改作業...')
    elif user == 3:
        print('查詢作業...')
    else:
        print('輸入值不正確')

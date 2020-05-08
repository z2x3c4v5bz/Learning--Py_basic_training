# hw03_02
season = int(input('請輸入一個1~12之間的月份: '))
if (season >= 3) and (season <= 5):
    print('春天')
elif (season >= 6) and (season <= 8):
    print('夏天')
elif (season >= 9) and (season <= 11):
    print('秋天')
elif (season == 12) or (season == 1) or (season == 2):
    print('冬天')
else:
    print('輸入錯誤！')
# hw03_03
nci = float(input('請輸入您的綜合所得淨額：'))
print('您所要繳交的所得稅額是：', end='')
if (nci <= 540000):
    print('%.1f' % (nci * 0))
elif (nci <= 1210000):
    print('%.1f' % (nci * 0.12))
elif (nci <= 2420000):
    print('%.1f' % (nci * 0.2))
elif (nci <= 4530000):
    print('%.1f' % (nci * 0.3))
elif (nci <= 10310000):
    print('%.1f' % (nci * 0.4))
else:
    print('%.1f' % (nci * 0.45))
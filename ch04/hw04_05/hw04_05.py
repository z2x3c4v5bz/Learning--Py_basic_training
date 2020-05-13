# hw04_05
import random

while True:
    l = random.randint(0, 1)
    r = random.randint(0, 1)
    print('%d;%d' % (l, r))
    if l + r == 1:
        print('你擲出了聖筊')
        break


'''

1;1
0;0
1;1
0;0
1;1
0;0
0;1
你擲出了聖筊

'''

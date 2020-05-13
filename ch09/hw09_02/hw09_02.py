# hw09_02
passage = ('端湯上塔，塔滑湯灑，湯燙塔')
passet = set(passage)
print(passage)
for char in passet:
    print('{0} 共使用 {1} 次'.format(char, passage.count(char)))


'''

端湯上塔，塔滑湯灑，湯燙塔
燙 共使用 1 次
滑 共使用 1 次
端 共使用 1 次
， 共使用 2 次
上 共使用 1 次
灑 共使用 1 次
塔 共使用 3 次
湯 共使用 3 次

'''

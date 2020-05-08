# hw09_02
passage = ('端湯上塔，塔滑湯灑，湯燙塔')
passet = set(passage)
print(passage)
for char in passet:
    print('{0} 共使用 {1} 次'.format(char, passage.count(char)))
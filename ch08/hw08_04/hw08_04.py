# hw08_04

flag = True

w = str(input("輸入英文單字："))

for i in range(int(len(w)/2)):
    if w[i] != w[-(i+1)]:
        flag = False

if flag:
    print("{}是廻文".format(w))
else:
    print("{}不是廻文".format(w))

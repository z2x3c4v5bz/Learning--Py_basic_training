# hw10_03
import os

userpath = input('請輸入資料夾路徑 : ')
userfile = userpath + input('請輸入檔案名稱 : ')

if not os.path.exists(userpath):
    os.mkdir(userpath)
if not os.path.isfile(userfile):
    uFile = open(userfile, 'w', encoding='utf-8')
    uFile.write('姓名      國文  英語\n')
    uFile.write('=' * 20)
    uFile.write('\n')
    uFile.close()

uFile = open(userfile, 'a+', encoding='utf-8')

while True:
    adddata = input('是否要輸入資料?(y/n) : ')
    if adddata == 'n':
        break
    newdata = input('輸入學生姓名,國文,英語成績 : ')
    newdata = newdata.split(',')
    uFile.write('{0} {1}  {2}\n'.format(newdata[0].ljust(6), newdata[1].rjust(4), newdata[2].rjust(4)))

uFile.seek(0)
print(uFile.read())
uFile.close()
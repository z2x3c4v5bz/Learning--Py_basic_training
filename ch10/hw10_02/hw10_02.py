# hw10_02
import os

if os.path.exists('poem1.txt'):
    p1 = open('poem1.txt', 'r', encoding = 'utf-8')
else:
    p1 = open('poem1.txt', 'w+', encoding = 'utf-8')
    p1.write('山中雜詩\t\t吳均\n')
    p1.write('山 際 見 來 煙 。\n')
    p1.write('竹 中 窺 落 日 。\n')
    p1.write('鳥 向 簷 上 飛 。\n')
    p1.write('雲 從 窗 裏 出 。')
if os.path.exists("poem2.txt"):
    p2 = open('poem2.txt', 'r', encoding = 'utf-8')
else:
    p2 = open('poem2.txt', 'w+', encoding = 'utf-8')
    p2.write('贈范曄詩\t\t陸凱\n')
    p2.write('折 花 逢 驛 使 ，\n')
    p2.write('寄 與 隴 頭 人 。\n')
    p2.write('江 南 無 所 有 ，\n')
    p2.write('聊 贈 一 枝 香 。')

p1.seek(0)
p2.seek(0)
p3 = open('poem3.txt', 'w', encoding = 'utf-8')

for line in p1:
    p3.write(line)
p3.write('\n\n')
for line in p2:
    p3.write(line)

p1.close()
p2.close()
p3.close()
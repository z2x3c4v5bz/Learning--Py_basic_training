# hw11_01
import matplotlib.pyplot as plt

font = {'family':'DFKai-SB'}
plt.rc('font', **font)

listX = [2015, 2016, 2017, 2018, 2019, 2020]
listManagementY = [500, 512, 430, 480, 490, 530]
listDesignY = [430, 500, 510, 300, 320, 520]
listComputerY = [330, 400, 410, 500, 520, 580]

plt.plot(listX, listManagementY, ls='-.', lw=4, label="商管")
plt.plot(listX, listDesignY, lw=4, label="設計")
plt.plot(listX, listComputerY, lw=4, ls=':', label="資電")
plt.title("碁峰科大歷年招生錄取分數")
plt.xlabel("年度")
plt.ylabel("分數")
plt.ylim(0, 700)
plt.legend()
plt.show()
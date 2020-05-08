# hw11_02
import matplotlib.pyplot as plt

font = {'family' : 'DFKai-SB'}
plt.rc('font', **font)
listPercent = [25.2, 31.8, 43]
listDep = ["商管", "資電", "設計"]
listExplode = [0, 0, 0.1]
plt.pie(listPercent, shadow=True, labels=listDep, explode=listExplode, autopct='%2.1f%%')
plt.title('碁峰科大招生員額比例')
plt.axis('equal')
plt.legend()
plt.show()
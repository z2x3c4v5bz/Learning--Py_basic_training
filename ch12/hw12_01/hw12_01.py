# hw12_01
import tkinter as tk

def funcOK():
    vPrincipal = principal.get()
    vAiRate = aiRate.get()
    i = vPrincipal / 100 * vAiRate
    lblResult['text'] = '利息是 {0} 元'.format(i)

win = tk.Tk()
win.title('銀行利息計算')
win.geometry('200x120')
principal = tk.IntVar()
aiRate = tk.DoubleVar()
lbl01 = tk.Label(win, text='本金', padx=10, pady=8)
lbl01.grid(row=0, column=0)
lbl02 = tk.Label(win, text='年利率', padx=10, pady=8)
lbl02.grid(row=1, column=0)
txtPrincipal = tk.Entry(win, width=15, textvariable=principal)
txtPrincipal.grid(row=0, column=1)
txtAiRate = tk.Entry(win, width=15, textvariable=aiRate)
txtAiRate.grid(row=1, column=1)
btnOK = tk.Button(win, text='確定', command=funcOK)
btnOK.grid(row=3, column=0)
lblResult = tk.Label(win, text='', padx=10, pady=8)
lblResult.grid(row=3, column=1)
win.mainloop()
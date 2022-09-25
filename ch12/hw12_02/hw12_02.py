# hw12_02
import tkinter as tk
from tkinter import messagebox as msgbox


def funcCalcu():

    vCurrency = currency.get()

    if vCurrency == 'TWD2USD':

        ans = money.get() / exchangeRate.get()
        result = '台幣{0}元可兌換成美金{1:.1f}元'.format(money.get(), ans)

    else:

        ans = money.get() * exchangeRate.get()
        result = '美金{0}元可兌換成台幣{1:.1f}元'.format(money.get(), ans)
        
    msgbox.showinfo('台幣和美金相互兌換', result)


if __name__ == '__main__':

    win = tk.Tk()
    win.title('台幣和美金相互兌換')
    win.geometry('250x150')

    lbl01 = tk.Label(win, text='請輸入金額', padx=10, pady=8)
    lbl01.grid(row=0, column=0)
    lbl02 = tk.Label(win, text='請輸入美金匯率', padx=10, pady=8)
    lbl02.grid(row=1, column=0)
    money = tk.IntVar()
    txtMonry = tk.Entry(win, width=15, textvariable=money)
    txtMonry.grid(row=0, column=1)
    exchangeRate = tk.DoubleVar()
    txtExchangeRate = tk.Entry(win, width=15, textvariable=exchangeRate)
    txtExchangeRate.grid(row=1, column=1)
    currency = tk.StringVar()
    currency.set('TWD2USD')
    radTW = tk.Radiobutton(win, text='台幣換美金', variable=currency, value='TWD2USD')
    radTW.grid(row=2, column=0)
    radUS = tk.Radiobutton(win, text='美金換台幣', variable=currency, value='USD2TWD')
    radUS.grid(row=2, column=1)
    btnCalcu = tk.Button(win, text='兌換', command=funcCalcu)
    btnCalcu.grid(row=3, column=0)
    win.resizable(width=False, height=False)
    win.mainloop()
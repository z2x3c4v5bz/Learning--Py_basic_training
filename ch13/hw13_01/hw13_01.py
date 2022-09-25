# hw13_01
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':

    urlstr = 'https://www.taiwanlottery.com.tw/index_new.aspx'
    responseObj = requests.get(urlstr)
    bs = BeautifulSoup(responseObj.text, 'html.parser')

    #print(bs.title.text)

    data = bs.select('.contents_box02')
    link = data[2].find_all('div')

    print('\n本期大樂透開獎結果如下 :')
    print('號碼順序 :', end=' ')

    for n in range(9, len(link) - 1):
        print(link[n].text, end=' ')

    print('\n特別號碼 :', end=' ')
    print(link[-1].text)

    input("Press Enter to continue . . .")


''' Output

本期大樂透開獎結果如下 :
號碼順序 : 01  05  08  11  35  36
特別號碼 : 26
Press Enter to continue . . .

'''

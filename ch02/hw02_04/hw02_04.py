# hw02_04


if __name__ == '__main__':

    distence = float(input('請輸入距離(單位公尺)：'))
    print('')

    score = float(input('請輸入成績(單為秒)：'))
    print('速度為：%.2f百公尺/分鐘' % (distence / score * 60 / 100))


''' Output

請輸入距離(單位公尺)：100

請輸入成績(單為秒)：13
速度為：4.62百公尺/分鐘

'''

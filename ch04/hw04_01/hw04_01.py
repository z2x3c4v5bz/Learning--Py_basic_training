# hw04_01


if __name__ == '__main__':

    x = 1

    for i in range(5):

        for j in range(5 - x):
            print(' ', end='')

        for k in range(x, 0, -1):
            print(k, end='')

        x += 1

        if x <= 5:

            print('')

        else:

            break


''' Output

    1
   21
  321
 4321
54321

'''

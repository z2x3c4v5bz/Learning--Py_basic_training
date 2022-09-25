# hw06_03
import random


def makesentence():

    subjects = ['Dog', 'Cat', 'Monkey', 'Pig', 'Fox']
    verbs = ['walks', 'runs', 'jumps']
    advs = ['slowly', 'quickly']

    print('%s %s %s.' % (random.choice(subjects), random.choice(verbs), random.choice(advs)))


if __name__ == '__main__':

    for i in range(5):
        makesentence()


''' Output

Cat walks quickly.
Fox jumps slowly.
Monkey jumps slowly.
Pig jumps slowly.
Monkey walks quickly.

'''

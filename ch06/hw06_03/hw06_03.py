# hw06_03
import random

def makesentence():
    subjects = ['Dog', 'Cat', 'Monkey', 'Pig', 'Fox']
    verbs = ['walks', 'runs', 'jumps']
    advs = ['slowly', 'quickly']

    print('%s %s %s.' % (random.choice(subjects), random.choice(verbs), random.choice(advs)))

for i in range(5):
    makesentence()
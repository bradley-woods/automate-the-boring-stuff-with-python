# Automate the Boring Stuff with Python
# Chapter 4 - Lists: Coin Flip Streaks

import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    results = []
    for flip in range(100):    
        flip = random.randint(0, 1)
        if flip == 1:
            results.append("heads")
        else:
            results.append("tails")

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 0
    for flip in range(len(results)-1):
        if results[flip] == results[flip+1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

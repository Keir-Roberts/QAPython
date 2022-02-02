# A simple module for rolling a getting a number between 1-6, a certain number of times.

from random import randint


def dice(amount):
    roll = []
    for digits in range(0, amount):
        roll.append(randint(1, 7))
    return roll

from random import randint


def dice(amount):
    roll = []
    for digits in range(0, amount):
        roll.append(randint(1, 7))
    output = str(roll)
    return output


print(dice(2))

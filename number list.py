# For each number between 2000 and 3200 inclusive, if it is a multiple of 7 but not 5, print it
numlist = []
for number in range(2000, 3201):
    if number%7 == 0 and  number%5 > 0:
        numlist.append(number)

print(numlist)

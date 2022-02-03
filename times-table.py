# A piece of code to generate n amounts of values in x times tables.

# Initial error code and taking inputs

try:
    while True:
        num = int(input("How many values in each table? "))
        amount = int(input("How many times tables do you want? "))
        break
except ValueError:
    print("Only input integers please! ")

    
# A function that creates a list to store each times table
# A nested if statement that creates a new list,
# fills the list with the multiplication of current number between 1 and x,
# with numbers between 1 and n, then adds a string of that list into biglist,
# seperated by spaces, before repeating with a 1 higher digit.
# When all timestables are made, biglist is coverted into a string,
# seperated by new lines which is returned as output


def timestable(n, x):
    biglist = []
    for digit in range(1, x+1):
        list = []
        for number in range(1, n+1):
            list.append(str(digit * number))
        biglist.append("\t".join(list))
    output = "\n".join(biglist)
    return output


print(timestable(num, amount))

# A piece of code to generate n amounts of values in x times tables.

#Initial error code and taking inputs

try:
    while True:
        n = int(input("How many values in each table? "))
        x = int(input("How many times tables do you want? "))
        break
except ValueError:
    print("Only input integers please! ")

# A nested if statement that creates a new list, 
# fills it with the multiplication of the current number between 1 and x, with the numbers between 1 and n,
# then prints off that list as a string seperated by spaces, before repeating with a 1 higher digit.

for digit in range(1, x+1):
    list = []
    for number in range(1, n+1):
        list.append(str(digit * number))
    print(" ".join(list))

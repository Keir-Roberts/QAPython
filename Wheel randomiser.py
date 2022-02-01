from random import randint
bootcamp = ["Aaron", "Bhavneesh", "Carlos", "Dovydas", "Emilia", "Filippo", "Habon", "Jeffrey", "Joe", "Kalliszta", "Liam", "Louisa", "Martyn", "Lateef", "Omkar", "Paige", "Paula", "Simon"]
people = input("How many people per group? ")
if int(people) > len(bootcamp):
    print("Too many people") and quit()

y = len(bootcamp)
z = 0
groups = {}
while y//int(people)>z:
    x = int(people)
    group = []
    
    while x > 0:
        choice = randint(0,x)
        result = bootcamp.pop(choice)
        group.append(result)
        x -= 1
    groups[f"group{z + 1}"] = group
    z += 1
group = []
for members in bootcamp:
    group.append(members)
groups[f"group{z + 1}"] = group
print(groups)
# Create a code that returns a boolean of True if a given string ends with 'py'
# and false otherwise.

def pyend(phrase):
    return (phrase.lower()).endswith("py")


print(pyend(input("Write a string")))

# A program to roughly talk back to you
greeting = input("Hello there! ")
if greeting == greeting.upper():
    print("Woah! no need to shout!")
elif "name" in greeting.lower():
    print("huh.. I dont have a name, guess my creator is lazy")
elif "you" in greeting.lower() and ("how" in greeting.lower() or "what" in greeting.lower() or "are" in greeting.lower()):
    print("Im not here to answer your questions buddy")
elif "hello" in greeting.lower() or "hi" in greeting.lower():
    print("Hello to you too...")
elif "goodbye" in greeting.lower() or "bye" in greeting.lower():
    print("okay, see ya I did not want to talk to you anyway")
elif "code" in greeting.lower():
    print("Do you really start every conversation by asking how someone works? thats kinda rude")
else:
    print("cool, you're being original!")
    
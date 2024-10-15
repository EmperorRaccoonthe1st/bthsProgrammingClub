# While Loops run "while something is true"
# Can be a variable or condition or function ect
# Handy for running a program but in general very inefficient 


# # For Example 
# while True:
#     print("Hello")

# Must start with a "while", then the condition, then a semicolon
# while (condition):
#  indented code blah blah
#   all code a loop must be indented
#   in python at least

# "Break" ends the loop and "pass" make it iterate again

var = 0

while var < 100:
    print(f"This is var: {var}")
    var += 1

while True:
    inputVar = str(input("Type quit to end the program: "))
    if inputVar == "quit":
        break


while True:
    inputVar = str(input("Type Hello! to keep the loop running: "))
    if inputVar == "Hello!":
        print("Hello to you too!")
        pass
    else:
        break
    




















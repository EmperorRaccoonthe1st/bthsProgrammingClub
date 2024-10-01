# Conditionals test to see if somenthing is true or not
# if a certain value equals another value

# if {condition}:
#   code
# else:
#   more code

var = "hello!!!!"

if var == "hello!!!!":
    print("It works! It works! It works!")

print("###") 

if var == "Not hello :(":
    print("It works! It works! It works!")
else:
    print("It didn't work >:{")

print("###") 

# also works with numbers

varInt = 45

if varInt > 30:
    print("It works! It works! It works!")
else:
    print("It didn't work >:{")

# not equals 🤔🤔🤔

if var != "hello!!!!":
    print("It didn't work >:{")

# notice how this code achieved the same effect as the else block; basically flipped it
# all of these work: <, >, <=, and >=

print("###")

# Nest Em!!

userInput = int(input())

if userInput > 50:
    print("Your input was greater than 50")
    if userInput < 100:
        print("And less than 100")
    else:
        print("But not less than 100")
else:
    print("Your input was less than 50")
    if userInput < 0:
        print("And apparently negative too 😳")
    else:  
        print("But not negative 😥")

print("###")

# some more nesting
grade = int(input("Enter your grade level: "))

if grade == 9:
    print("You are a freshman.")
else:
    if grade == 10:
        print("You are a sophomore.")
    else:
        if grade == 11:
            print("You are a junior.")
        else:
            if grade == 12:
                print("You are a senior.")
            else:
                print("Invalid grade. Please enter a number between 9 and 12.")

print("###")

# Elif literally means else--> if

if grade == 9:
    print("You are a freshman.")
elif grade == 10:
    print("You are a sophomore.")
elif grade == 11:
    print("You are a junior.")
elif grade == 12:
    print("You are a senior.")
else:
    print("Invalid Grade")

# They do the same thing

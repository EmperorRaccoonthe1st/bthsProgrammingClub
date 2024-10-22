# Functions are blocks of code that we save for later use
# Basically code we dont want to have to copy over and over
# In python you define them like this
    # def functionName(Parameters):
    #  Then an indent with the code

def myExampleFunc(parameter1, parameter2):
    pass



def repeatTenTimes(text):
    for i in range(10):
        print(text)


# Then you call them by just stating their name and their parameters in parenthesis

getInput = str(input("Put your input here: "))

repeatTenTimes(getInput)

for i in range(10):
    print(getInput)





def funcy(var):
    pass





# Now you can specify what typw the parameter must be to ensure type safty and minimize errors

def typeSafeFunc(text:str, loopNum:str, isExlame:bool):
    for i in range(loopNum):
        print(text)
        if isExlame == True:
            print(text+"!")

# These parameters are then forced to be whatever type they are

typeSafeFunc("I'm Owen", 50, True)






# Often youll have functions that enact a process and generate a value that you want back
# based on your parameters
# The "return" will end a function a spit out a value

def spitter(text: str):
    newText = text + "!!!!"
    return newText

# now I have to print the result of the function
print(spitter("Hey"))

def isFruit(fruitName:str):
    pass












# You can also specify the result of the function too, to make your code more readable
# Important to do when working with others, or in large projects

def returnsText(num:int) -> str:
    output = ""
    for i in range(num):
        output += "a"
    return(output)

print(returnsText(1000))







print("###")

# Write a Python code to remove characters from a string from 0 to n and return a new string.

# Have a string
# Get input from the user: the characters to remove, what part of the string to remove from - Number
# iterate through the string 
# check if the character is in the string
# remove character
# print final string 

def removeChar(stringInput: str, char: str, rang: int) -> str:
    newString = ""
    print(f"String: {len(stringInput)}")
    listString = list(stringInput)
    for i in range(rang):
        currentLetter = stringInput[i]
        if currentLetter in list(char):
            for o in range(len(listString)):
                if listString[o] == currentLetter:
                    listString.remove(o)
        stringInput = ""
        for element in listString:
            stringInput += element
    return stringInput



print(removeChar("I'm Owen and I love to code!", "aeiou", 27))

input = input()
for i in range(len(input)-1):
    print(removeChar(input, "aeiou", i))























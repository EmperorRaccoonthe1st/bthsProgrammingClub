import random
print("#")
print("#")

inputName = []
inputHobby = []

for i in range(5):
    inputName += [input("Input a name: ")]
    inputHobby += [input("Input a hobby: ")]
print(inputName)

for i in inputName:
    print(f"My name is {i} and I like {inputHobby[random.randint(0, 4)]}")





















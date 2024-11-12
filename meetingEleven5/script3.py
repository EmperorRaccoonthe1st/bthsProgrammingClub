print("###")

x = 10
y = 5
z = x + y
print(z)

print(x+y)

x = x + y
print(x)

x = 10
x -= y
print(x)


numList = [5, 10, 15, 20, 25]
x = numList[0]
y = numList[1]
z = x + y
print(z)
print(numList[0] + numList[1])
x += numList[1]
print(x)

finalNum = 0
for item in numList:
    finalNum += item
else:
    print(finalNum)

x = 0
finalNum = 0
while x < len(numList):
    finalNum += numList[x]
    x += 1

else:
    print(finalNum)


x = 10
y = 5

def addFunc(num1: int, num2:int) -> int:
    return num1 + num2


print(f"My num: {addFunc(25, 25)}")












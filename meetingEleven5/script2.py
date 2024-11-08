# Rewrite it with a for and while loop
num = 0
for i in range(6):
    print(num)
    num = num + 1

num = 0
for i in range(6):
    print(num)
    num -= 1

def printTimes(num:int):
    for i in range(num):
        print(i)

printTimes(10)

var = 1

while var < 6:
    print(var)
    var += 1

var = 1
while var <= 5:
    print(var)
    var += 1

var = 1
while var != 6:
    print(var)
    var += 1

var = 0
while var != 5:
    print(var + 1)
    var += 1

var = 1
while True:
    print(var)
    if var == 5:
        break
    else:
        var += 1
#  








print("#")
# Write a Python code to accept a string from the user
#  and display characters present at an even index number.

# hello
# 01234

# Get User Input
# run a for loop over it
# check even
# add it to a list of the letters that are even
# print that list

result = ""
li = list(input())

for i in range(len(li)):
    if i % 2 == 0:
        result += li[i] + " "
else:
    print(result)

























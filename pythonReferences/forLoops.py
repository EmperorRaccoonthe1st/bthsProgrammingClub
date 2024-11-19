# for loops run "for" certain period of time
# for all the times in a list
# for a certain amout
# they are used to interate over items in a programm


for i in range(30):
    print(f"Hello x{i}")

print("#")
print("#")
print("#")

# the for loop starts with "for"
# then you define an index varible
# then the item that you will iterate over

# for example in the loop above the "i" was the index varible
# can be named however you want tho
# index varibles track the amount of times the for loop has looped
# starts at 0

randomNumber = 5

for index_varible in range(randomNumber):
        print(str(index_varible) + "st time")


# here is a loop iterated over a list
# when the iteration is a list the index is not a number 
# but is instead the actual item that the loop is iterating over

print("#")
print("#")
print("#")

list = ["apple", "bannana", "cookie"]

for i in list:
      print(f"I like {i}s")

# for loops require a range of something, whether thats a list or a number
# to make them run for a certain amount of times use the "range()" function

print("#")
print("#")
print("#")

for i in range(10):
      print("see now it will go for ten times")

# select the line below and press "crt+/" to uncomment
# for i in 10:
#       print("this will throw an error, python doesn't understand a plain numeral")


# you can iterate over string tho
# it'll run a loop for each character
# put your name in the var below

print("#")
print("#")
print("#")

strVar = "Oween"

for i in strVar:
      print(i)


# you can nest loops, if you do tho make sure they have different index varibles

for i1 in strVar:
      for i2 in strVar:
            print(f"i2:{i2}")
            print(f"i1:{i1}")












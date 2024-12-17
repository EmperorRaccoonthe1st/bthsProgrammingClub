print("###")
name: str = input("What is your name?")
fileName: str = name + "XmasLetter.txt"

with open(fileName, "w") as file:
    file.write("Hey!")
    file.write(" Whats going on!.\n")
    file.write("Merry Xmas!!!!")
    file.write("\nDoes this work?")































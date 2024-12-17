print("###")
name: str = input("What is your name?")
mainFileName: str = name + "XmasLetter.txt"

def main():
    startLetter(mainFileName)

def startLetter(fileName:str):
    with open(fileName, "w") as file:
        file.write("Hey!")
        file.write(" Whats going on!.\n")
        file.write("Merry Xmas!!!!")
        file.write("\nDoes this work?")

def appendSmallTalk(fileName:str):
    pass
    # open file w/a
    # write into it the "small talk"
    # mad libs and decision trees

def appendBrag(fileName:str):
    with open(fileName, "a") as file:
        pass






























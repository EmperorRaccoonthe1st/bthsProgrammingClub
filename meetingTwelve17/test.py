print("###")
name: str = input("What is your name? ")
mainFileName: str = name + "XmasLetter.txt"



def startLetter(fileName:str):
    with open(fileName, "w") as file:
        file.write(" .-""-. \n")
        file.write("/,..___\ \n")
        file.write("() (_____) \n")
        file.write("  (/-@-@-\) \n")
        file.write("  {`-=^=-'} \n")
        file.write("  {  `-'  } \n")
        file.write("   {     } \n")
        file.write("    `---' \n")
        file.write("123 North Pole Ln, North Pole\n")
        file.write("Dear Santa,\n")
        file.write("\n")
def appendSmallTalk(fileName:str):
    questionList:list[str] = []
    for i in range(4):
        questionList.append(input("Input a question to ask Santa: "))
    with open(fileName, "a") as file:
        file.write("I'm so happy that its christmas now.\n")
        file.write("I've had a great year so far!\n")
        file.write("How are things at the north pole?\n")
        for q in questionList:
            file.write(q + "\n")


def appendBrag(fileName:str):
    if input("Have you been good this year? y/n ") == "y":
        pass
    else:
        pass


def main():
    startLetter(mainFileName)
    appendSmallTalk(mainFileName)



















main()





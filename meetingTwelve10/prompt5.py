# credit cards have 16 digits btw
# 5835105705131100
# Get input
# make input a list
# add last four characters to a list of 12 #'s
# return the hidden number
print("###")

def hideCreditNum(creditNum: str) -> str:
    # hiddenNum = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
    hiddenNum = "############"
    endNums = ""
    creditNumList = list(creditNum)
    for i in range(4):
        endNums += creditNumList[-i-1]
    return hiddenNum.join(reversed(endNums))









def main():
    while True:
        inputVar = input()
        if inputVar.lower() == "quit":
            break
        print(f"Your credit card number is: {hideCreditNum(inputVar)}")













main()
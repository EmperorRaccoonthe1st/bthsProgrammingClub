# get input
# run through for loop
# check if index variableis a vowel
# if so add to a count variable 
# return count
print("###")

def countVowel(word: str) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count

def main():
    while True:
        inputVar = input()
        if inputVar.lower() == "quit":
            break
        print(f"There are {countVowel(inputVar)} vowels in {inputVar}")





main()





# for this activity I will provide a data set
# You all will need to sort through this data set 
# Utilizing for and while Loops, as well as everyting else we have learned



data = [
    ["Alice", "Smith", 30, "Software Engineer", "Reading", 80000],
    ["Bob", "Johnson", 25, "Data Scientist", "Hiking", 75000],
    ["Charlie", "Brown", 35, "Marketing Manager", "Cooking", 90000],
    ["David", "Lee", 40, "Product Manager", "Gaming", 100000],
    ["Eve", "Miller", 28, "Designer", "Painting", 65000],
    ["Frank", "Davis", 32, "Sales Representative", "Traveling", 70000],
    ["Grace", "Wilson", 27, "Financial Analyst", "Yoga", 85000],
    ["Henry", "Taylor", 38, "Project Manager", "Photography", 95000],
    ["Ivy", "Anderson", 29, "Teacher", "Gardening", 60000],
    ["Jack", "Thomas", 33, "Business Analyst", "Music", 82000],
    ["Karen", "Harris", 31, "Human Resources Manager", "Dancing", 78000],
    ["Leo", "Martin", 24, "Software Developer", "Biking", 72000],
    ["Maria", "Garcia", 36, "Nurse", "Baking", 68000],
    ["Nathan", "Martinez", 26, "Data Analyst", "Swimming", 74000],
    ["Olivia", "Hernandez", 34, "Accountant", "Reading", 84000],
    ["Paul", "Lopez", 37, "Lawyer", "Golfing", 120000],
    ["Quinn", "Gonzalez", 28, "Marketing Coordinator", "Painting", 62000],
    ["Rachel", "Wright", 35, "Teacher", "Reading", 65000],
    ["Sarah", "Scott", 32, "Sales Manager", "Traveling", 85000],
    ["Thomas", "Nelson", 29, "Software Engineer", "Gaming", 80000],
    ["Ursula", "Carter", 30, "Financial Analyst", "Yoga", 75000],
    ["Victor", "Phillips", 33, "Project Manager", "Photography", 90000],
    ["Wendy", "Roberts", 27, "Teacher", "Gardening", 62000],
    ["Xavier", "Jordan", 31, "Business Analyst", "Music", 85000],
    ["Yolanda", "Patterson", 25, "Human Resources Manager", "Dancing", 70000],
    ["Zachary", "Simmons", 28, "Software Developer", "Biking", 75000]
]

# Write me a program that takes this data and outputs these metrics:
# Amount of People, Highest Salary, Oldest Person, Youngest Person
# I also want it to take a response from the user, asking if their is a person in the dataset that has a specific hobby

while True:
    inputVar = str(input("What do you want to do: "))
    if inputVar == "quit":
        break
    elif inputVar == "1":
        amount = 0
        for x in data:
            amount += 1
        print("###")
        print("###")
        print("###")
        print(f"The amount of people in the dataset is {amount}")
    elif inputVar == "2":
        hSal = 0
        for i in data:
            newSal = i[-1]
            if newSal > hSal:
                hSal = newSal
        print(f"The highest salary is {hSal}")
    elif inputVar == "3":
        hAge = 0
        for i in data:
            newAge = i[2]
            if newAge > hAge:
                hAge = newAge
        for i in data:
            if i[2] == hAge:
                print(f"The oldest person is {i[0]} {i[1]}")
    elif inputVar == "4":
        print("Youngest")
        sAge = 100
        for i in data:
            newAge = i[2]
            if newAge < sAge:
                sAge = newAge
        for i in data:
            if i[2] == sAge:
                print(f"The youngest person is {i[0]} {i[1]}")
    elif inputVar == "5":
        hobby = str(input("Hobby: "))
        for i in data:
            if i[4] == hobby:
                print(f"{i[0]} {i[1]} has {hobby} as their hobby")
                break
        else:
            print(f"No one has the hobby of {hobby}")

























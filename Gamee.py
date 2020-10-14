# stone paper sissor

import random

chance = 10
cpoint = 0
upoint = 0

while (chance != 0):
    lst = ["stone", "paper", "scissor"]

    choice = random.choice(lst)
    comp = choice


    user = input("Enter your choice \nstone\npaper\nscissor\n")
    if comp == user:
        print("Computer's answer is " ,comp)
        print("it is a tie")
        chance = chance - 1
        print("Your score is : ", upoint)
        print("Computer's score is : ",cpoint)
        print("No. of chances left are : ",chance)
        continue
    elif comp == "stone" and user == "paper":
        print("Computer's answer is " ,comp)
        upoint = upoint + 1
        chance = chance - 1
        print("Your score is : ", upoint)
        print("Computer's score is : ",cpoint)
        print("No. of chances left are : ",chance)
        continue
    elif comp == "stone" and user == "scissor":
        print("Computer's answer is ", comp)
        chance = chance - 1
        cpoint = cpoint + 1
        print("Your score is : ", upoint)
        print("Computer's score is : ",cpoint)
        print("No. of chances left are : ",chance)
        continue
    elif comp == "paper" and user == "stone":
        print("Computer's answer is ", comp)
        chance = chance - 1
        cpoint = cpoint + 1
        print("Your score is : ", upoint)
        print("Computer's score is : ",cpoint)
        print("No. of chances left are : ",chance)
        continue
    elif comp == "paper" and user == "scissor":
        print("Computer's answer is ", comp)
        chance = chance - 1
        upoint = upoint + 1
        chance -= 1
        print("Your score is : ", upoint)
        print("Computer's score is : ",cpoint)
        print("No. of chances left are : ",chance)
        continue
    elif comp == "scissor" and user == "stone":
        print("Computer's answer is ", comp)
        chance = chance - 1
        upoint = upoint + 1
        chance -= 1
        print("Your score is : ", upoint)
        print("Computer's score is : ",cpoint)
        print("No. of chances left are : ",chance)
        continue
    elif comp == "scissor" and user == "paper":
        print("Computer's answer is ", comp)
        chance = chance - 1
        cpoint = cpoint + 1
        print("Your score is : ", upoint)
        print("Computer's score is : ",cpoint)
        print("No. of chances left are : ",chance)
        continue
    else:
        print("invalid")
        continue

if cpoint>upoint:
    print("\n\nComputer is the winner")
elif upoint>cpoint:
    print("\n\nCongratulations you are the winner")
else:
    print("It is a tie")

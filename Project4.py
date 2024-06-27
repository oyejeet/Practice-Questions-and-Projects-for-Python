# Stone Paper Scissirs Game

# Check how many times the user gets it correct and how many times does the computer gets it correct.

import random # This imports the random module, which will be used to generate random choices for the computer_choose.

user_score = 0
computer_score = 0

options = ["stone","paper","scissors"]


while True: # This starts an infinite loop until the user quits it.

    user_input = input("Pick one from Stone/Paper/Scissors or q to Quit : ").lower()
    if (user_input == "q"):
        break
    
    if (user_input not in options): # not in is a keyword
        print("Please spell Correctly bro.")
        continue                    # Will skip the rest of the loop and will ask the user again

    random_int = random.randint(0,2) # It goes from 0 to 2 and will be using it as the index no.

    computer_choose = options[random_int]
    print("Computer Choosed :",computer_choose +".")

    if(user_input == "stone" and computer_choose == "scissors"):
        print("Letsss Gooo! You won")
        user_score += 1

    elif(user_input == "paper" and computer_choose == "stone"):
        print("Letsss Gooo! You won")
        user_score += 1

    elif(user_input == "scissors" and computer_choose == "paper"):
        print("Letsss Gooo! You won")
        user_score += 1

    elif(user_input == computer_choose):
        print("Ohh! No points for this one.")

    else:
        print("Ahh! You lose :( ")
        computer_score += 1


print("Your Score is " + str(user_score) + ".")
print("Computer's Score is " + str(computer_score) + ".")
print("GoodBye!")
  

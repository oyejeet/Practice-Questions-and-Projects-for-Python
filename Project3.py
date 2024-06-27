# Number Guesser 

# Generate a random number and track how many times it take the user to guess it.

import random # imports the random module. This module contains functions and classes for generating random numbers, selecting random items, shuffling data, and more.

top_of_range = input("Type a number : ")

if(top_of_range.isdigit()):            # checks whether the entered number is digit or not.
    top_of_range = int(top_of_range)   

    if(top_of_range <= 0):
        print("Please enter a number greater than 0 next time. ")
        quit()

else:
    print("Please type a number next time.")
    quit()

random_int = random.randint(1,top_of_range) #This function returns a random integer between 1 and top_of_range .

guesses = 0

while True:
    guesses += 1
    
    user_guess = input("Make a guess : ")
    if(user_guess.isdigit()):
        user_guess = int(user_guess)

    else :
        print("Please type a number next time.")
        continue

    if(user_guess == random_int):
        print("WOW! you guessed it correctly.")
        break
    elif(user_guess > random_int):
        print("Oh! you are above the number")
    else:
        print("Oh! you are below the number")

print("You got it in ",guesses,"guesses")



        




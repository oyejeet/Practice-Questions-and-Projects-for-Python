# Quiz Game 
# Ask the user a bunch of questions and if they give us right answer to these questions we will add 1 to their score. At the end print the total score.

print("Welcome, everyone! Are you ready for an exciting quiz showdown? Let’s find out who knows the most!")

playing = input("Type 'yes' if you want to play : ")

if (playing.lower() != "yes"):
    quit()

print("Okay! Let's play : )")   
score = 0

answer = input("Which animal is known as the 'Ship of the Desert'? ")

if (answer.lower() == "camel"):
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What is the national bird of India? ")

if (answer.lower() == "peacock"):
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("Who was the first Prime Minister of India? ")

if (answer.lower() == "jawaharlal nehru"):
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("Which festival is known as the Festival of Lights? ")

if (answer.lower() == "diwali"):
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What is the capital of India? ")

if (answer.lower() == "delhi"):
    print("Correct!")
    score += 1

else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")

print("So you scored ",(score / 5)*100,"%")



  # Search if the word "majdoors" exists in the file PQnhavishyavani.txt or not.

def check_for_word():
    word = "majdoors"
    with open("/Users/indrajeetsinghbava/CODE /PQ16bhavishyavani.txt","r") as f:
        data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")

check_for_word()

# Method 2:

def check_for_word():
    word = "majdoors"
    with open("/Users/indrajeetsinghbava/CODE /PQ16bhavishyavani.txt","r") as f:
        data = f.read()
    if(word in data): #More accurate way of writing this.
        print("Found")
    else:
        print("Not Found")

check_for_word()
 

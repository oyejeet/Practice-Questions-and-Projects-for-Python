# WAF that replaces occurence of "you" with "We" in file in PQ16
def replace_word():
    with open("/Users/indrajeetsinghbava/CODE /PQ16bhavishyavani.txt","r") as f:

        data = f.read()
# here we converted the that file into a string by giving it a variable "data",and then we performed an operation that can be performed on strings i.e the replace()
    new_data = data.replace("you","We")
    print(new_data)

    with open("/Users/indrajeetsinghbava/CODE /PQ16bhavishyavani.txt","w") as f:

        f.write(new_data)

replace_word()
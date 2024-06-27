# WAF to find in which line of the file does the word "majdoors" occur first in file PQ16bhavishyavani.txt .
# Print -1 if word not found.

def check_for_line():
    word = "majdoors"
    data = True
    line_no = 1
    with open("/Users/indrajeetsinghbava/CODE /PQ16bhavishyavani.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1
check_for_line()
        



    

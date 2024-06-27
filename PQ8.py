# Usiing for loop Print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

list = [1,4,9,16,25,36,49,64,81,100]
for val in list:
    print(val)

# Search for a number x in this tuple using for loop:
# (1,4,9,16,25,36,49,64,81,100,36)

tup =  (1,4,9,16,25,36,49,64,81,100,36)
i = 0
x = 36
for el in tup:
    if(el == x):
        print("Founded the element at index no.",i)
    else:
     print("finding")
    i += 1
# Important Note: This process of searching is called as linear search.

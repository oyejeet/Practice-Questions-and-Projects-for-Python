# Using for & range()

# Print numbers from 1 to 100.

num = range(1,101)
for val in range(1,101):
    print(val)

# Print numbers from 100 to 1.

num = range(100,0,-1)
for val in range(100,0,-1):
    print(val)

# Print multiplication table of a number n:

n = int(input("Enter the number:"))
num = range(1,11)
for i in range(1,11):
    print(n,"X",i,"=",i * n)
# WAP to find sum of first n natural numbers.(using While)

sum = 0
n = int(input("Enter the number:"))
i = 1
while (i <= n ):
    sum = sum + i
    i = i+1
print("Sum of first",n,"numbers is:",sum)
   

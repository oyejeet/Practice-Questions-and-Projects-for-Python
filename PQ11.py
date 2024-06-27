# WAP to find the factorial of first n numbers.(using for)

n = int(input("Enter the number:"))

fact = 1
for i in range(1,n+1):
    fact = fact * i
    i = i+1
print("Factorial of",n,"is",fact)
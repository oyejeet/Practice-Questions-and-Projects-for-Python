# WAF to find the factorial of n.(n is the parameter)

def fact_num(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact) # prints the final result and hence is written outside the loop
    return fact 
fact_num(5)
fact_num(8)
    
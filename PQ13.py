# WAF to convert USD to INR

def conv_curr(USD):
    INR = 80 * USD
    print(USD,"USD = ", INR,"INR")
    return INR
conv_curr(2)
conv_curr(90)

# WAF where take a number n as input, if the number is even print "EVEN" & if the number is odd, the print "ODD"

def num_val(n):
    if(n % 2 == 0):
        print(n,"is EVEN no.")
    else:
        print(n,"is ODD no.")
num_val(5)
num_val(114)
    
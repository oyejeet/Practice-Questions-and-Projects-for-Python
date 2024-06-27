# Create an invoice for KALYAN JWELLERS .

print("KALYAN JWELLERS")

name = input("\nEnter your name : ")
gender = input("Enter your gender M or F : ").lower()
if(gender != "m" and gender != "f"):
    quit()
age = int(input("Enter your age : "))

product = input("\nEnter Product : ") # Ring was purchased
quant = int(input("Enter product gram : "))
current_price = 5752
print("current gold price (1 grm) : ",current_price,"Rupees")

gold_rate = quant * current_price
print("\nTOTAL GOLD RATE : ",gold_rate,"Rupees")

making_charges = 845
print("\nMaking charges (1 grm) : ",making_charges,"Rupees")

Tmaking_charges = quant * making_charges
print("Total Making Charges : ",Tmaking_charges,"Rupees")

purchase = gold_rate + Tmaking_charges
print("\nTOTAL AMOUNT : ",purchase,"Rupees\n")

if (gender == "M" and age > 21):
    if(purchase > 21000 and purchase < 31000):
        Discount = 20
        print("Discount = ",Discount,"%")
    elif(purchase > 31000 and purchase < 51000):
        Discount = 30
        print("Discount = ",Discount,"%")
    elif(purchase > 51000):
        Discount = 35
        print("Discount = ",Discount,"%")
    else:
        Discount = 0
        print("Discount = ",Discount,"[Shop more to avail Discounts Sir]")
    
elif(gender == "M" and age < 21):
    if(purchase > 21000 and purchase < 31000):
        Discount = 10
        print("Discount = ",Discount,"%")
    elif(purchase > 31000 and purchase < 51000):
        Discount = 20
        print("Discount = ",Discount,"%")
    elif(purchase > 51000):
        Discount = 25
        print("Discount = ",Discount,"%")
    else:
        Discount = 0
        print("Discount = ",Discount,"[Shop more to avail Discounts Sir]")   

elif(gender == "F" and age >21):
    if(purchase > 21000 and purchase < 31000):
        Discount = 25
        print("Discount = ",Discount,"%")
    elif(purchase > 31000 and purchase < 51000):
        Discount = 35
        print("Discount = ",Discount,"%")
    elif(purchase > 51000):
        Discount = 40
        print("Discount = ",Discount,"%")
    else:
        Discount = 0
        print("Discount = ",Discount,"[Shop more to avail Discounts MAM]")

elif(gender == "F" and age< 21):
    if(purchase > 21000 and purchase < 31000):
        Discount = 15
        print("Discount = ",Discount,"%")
    elif(purchase > 31000 and purchase < 51000):
        Discount = 25
        print("Discount = ",Discount,"%")
    elif(purchase > 51000):
        Discount = 30
        print("Discount = ",Discount,"%")
    else:
        Discount = 0
        print("Discount = ",Discount,"[Shop more to avail Discounts MAM]")

else:
    quit()

dis = (Discount/100) * gold_rate # Making charges not included for discount
dis_amt = gold_rate - dis
print("Dicounted Amount : ",dis_amt,"Rupees [Discount is only on TOTAL GOLD PRICE and not on Making Charges]")

net_amt = Tmaking_charges + dis_amt
print("\ntotal net amount : ",net_amt,"Rupees")


print("\n\nTHANKS FOR SHOPPING FROM KALYAN JWELLERS")













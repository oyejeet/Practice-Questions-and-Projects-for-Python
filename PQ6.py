# WAP to enter marks of 3 subjects from the user and store them in  a dictionary.Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("enter marks of phy :"))
marks.update({"physics" : x})

y = int(input("enter marks of chem :"))
marks.update({"Chem" : y})

z = int(input("enter marks of Maths :"))
marks.update({"Maths" : z})

print(marks)

# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)

list1 = [1,2,1]
list2 = [1,2,3]
list3 = ["r","a","c","e","c","a","r"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not a Palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("Palindrome")
else:
    print("Not a Palindrome")

copy_list3 = list3.copy()
copy_list3.reverse()

if(copy_list3 == list3):
    print("Palindrome")
else:
    print("Not a Palindrome")
        


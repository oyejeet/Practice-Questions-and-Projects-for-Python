# Write a recursive function to print all elements in a list. Hint: use list & index as parameters.


def val(list,idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    val(list, idx+1)

names = ["Sachiv Ji","Vidhayak","Rinki","Rinki ke Papa","Rinki ki mummy"]

val(names)
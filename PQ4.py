# store following word meanings in a python dictionary:
# table : "a piece of furniture" , "list of facts & figures"
# cat : "a small animal"


dict = {}
dict["table"]= ["a piece of furniture","list of facts & figures"] #if we remove square bracket from RHS i.e the value part it will automatically become a tuple.
dict["cat"] = "a small animal"
print(dict)

#other way is the normal way without using empty dictionary and saving the table key as list or tuple.
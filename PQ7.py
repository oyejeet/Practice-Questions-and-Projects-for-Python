# Figure out a way to store 9 and 9.0 as separate values in the set.(You can take help of built-in data types).

# first method is store one of them as string as:values ={9,"9.0"}
#other possible solution is using built in Data types
values = {("float",9.0),("int",9)} #stored as tuple but that string method mentioned in the above comment is much better. 
print(values)
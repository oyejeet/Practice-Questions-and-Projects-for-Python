# You are given a list of subjects for students. Assume one classroom is required for 1 subject. how many classrooms are needed by all students.

#"python", "java","c++","javascript","python","java","python","java","c++","c"

sub = {"python", "java","c++","javascript","python","java","python","java","c++","c"}
classrooms = None #this is the way we define a variable in python.
print(sub)
classrooms = len(sub)

print("no. of classrooms needed are :",str(classrooms))
#this is more advanced way of getting the no. of classrooms, instead we could have also just type print(len(sub)).
# Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student():
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
    
        print("My name is : ",self.name)
        print("My marks in three of the subjects are : ",marks)

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum = sum + val
        print("hi",self.name,"your average score is : ",sum/3)
    

student1 = Student("Indrajeet Singh is King",[97,93,95])  

student1.name = "Captain America"
student1.avg_marks() 
 
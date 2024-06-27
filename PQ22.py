# Define a Circle class to creaste a circle with radius r using the constructor. Deinfe an Area() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.


class Circle():
    def __init__(self,r):
        self.radius = r

    def Area_circle(self):
        
        self.area = 3.14 * (self.radius * self.radius)
        print("Area of the Circle with Radius ",self.radius,"is : ",self.area)

        return Circle(self.area)

    def Perimeter_Circle(self):
        self.perimeter = 2 * 3.14 * self.radius
        print("Perimeter of the Circle with Radius ",self.radius,"is : ",self.perimeter)

        return Circle(self.perimeter)

r1 = Circle(8)

r1.Area_circle()
r1.Perimeter_Circle()
    
# Parent class
class Shape:
    # Method to calculate area
    def area(self):
        pass


# Child class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Child class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Create objects
rectangle = Rectangle(10, 5)
circle = Circle(7)

# Call area() method for different objects
print("Area of Rectangle:", rectangle.area())
print("Area of Circle:", circle.area())
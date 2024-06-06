import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


shapes = [
    Circle(5),
    Rectangle(width=3, height=4),
    Circle(2),
    Rectangle(6, 7)
]

areas = [shape.calculate_area() for shape in shapes]

total_area = sum(areas)

print("The areas of shapes:", areas)
print("The total area of all shapes:", total_area)

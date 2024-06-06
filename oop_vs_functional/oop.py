import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


shapes = [
    Circle(5),
    Rectangle(3, 4),
    Circle(2),
    Rectangle(6, 7)
]

areas = [shape.calculate_area() for shape in shapes]

total_area = sum(areas)

print("Площади фигур:", areas)
print("Общая площадь:", total_area)

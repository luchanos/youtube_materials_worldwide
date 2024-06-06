import math
from functools import reduce


def triangle_area(radius):
    return math.pi * radius ** 2


def rectangle_area(width, height):
    return width * height


def calculate_area(shape):
    shape_type = shape[0]
    if shape_type == 'circle':
        return triangle_area(shape[1])
    elif shape_type == 'rectangle':
        return rectangle_area(shape[1], shape[2])
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")


shapes = [
    ('circle', 5),
    ('rectangle', 3, 4),
    ('circle', 2),
    ('rectangle', 6, 7)
]

areas = list(map(calculate_area, shapes))


total_area = reduce(lambda x, y: x + y, areas)

print("The areas of shapes:", areas)
print("The total area of all shapes:", total_area)

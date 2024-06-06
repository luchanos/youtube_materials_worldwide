import math
from functools import reduce


def circle_area(radius):
    return math.pi * radius ** 2


def rectangle_area(width, height):
    return width * height


def calculate_area(shape):
    shape_type = shape["type"]
    params = shape["params"]
    if shape_type == 'circle':
        return circle_area(params["radius"])
    elif shape_type == 'rectangle':
        return rectangle_area(params["length"], params["width"])
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")


shapes = [
    {"type": "circle", "params": {"radius": 5}},
    {"type": "rectangle", "params": {"length": 3, "width": 4}},
    {"type": "circle", "params": {"radius": 2}},
    {"type": "rectangle", "params": {"length": 6, "width": 7}}
]



areas = list(map(calculate_area, shapes))


total_area = reduce(lambda x, y: x + y, areas)

print("The areas of shapes:", areas)
print("The total area of all shapes:", total_area)

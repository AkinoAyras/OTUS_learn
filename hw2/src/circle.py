from figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f"Can't create circle")
        self.radius = radius
        self.name = 'circle'

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return (self.radius ** 2) * math.pi

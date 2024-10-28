from lab_python_opp.figure import Figure
from lab_python_opp.color import Color
import math

class Circle(Figure):

    FIGURE_TYPE = "Круг"

    @classmethod
    def getFigureType(cls):
        return cls.FIGURE_TYPE
    
    def __init__(self, radius, color):
        self.radius = radius
        self.fc = Color(color)

    def area(self):
        return math.pi * (self.radius**2)
    
    def __repr__(self):
        return '{} {} цвета с радусом {} и площадью {}'.format(
            Circle.getFigureType(),
            self.fc.color,
            self.radius,
            self.area()
        )
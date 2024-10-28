from lab_python_opp.figure import Figure
from lab_python_opp.color import Color

class Rectangle(Figure):

    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def getFigureType(cls):
        return cls.FIGURE_TYPE
    
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.fc = Color(color)

    def area(self):
        return self.width * self.height
    
    def __repr__(self):
        return '{} {} цвета со сторонами {} и {}, площадь равна {}'.format(
            Rectangle.getFigureType(),
            self.fc.color,
            self.width,
            self.height,
            self.area()
        )
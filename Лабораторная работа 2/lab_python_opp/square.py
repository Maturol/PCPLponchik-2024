from lab_python_opp.rectangle import Rectangle

class Square(Rectangle):
    
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width, color):
        super().__init__(width, width, color)

    def __repr__(self):
        return '{} {} цвета со стороной {} и площадью {}'.format(
            Square.get_figure_type(),
            self.fc.color,
            self.width,
            self.area()
        )
import abc

class Figure(abc.ABC):

    @abc.abstractmethod
    def area(self): pass

    @abc.abstractclassmethod
    def getFigureType(cls): pass
from lab_python_opp.rectangle import Rectangle
from lab_python_opp.circle import Circle
from lab_python_opp.square import Square
import art


def main():
    rex = Rectangle(25, 25, "Синий")
    circus = Circle(25, "Зелёный")
    squad = Square(25, "Красный")
    print(rex)
    print(circus)
    print(squad)
    art.tprint("PCPL","rnd-xlarge")

if (__name__ == "__main__"):
    main()
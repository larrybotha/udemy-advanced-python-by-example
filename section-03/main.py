from random import randint

from .geometry import Point, Rectangle

if __name__ == "__main__":
    lower_left = Point(randint(0, 9), randint(0, 9))
    top_right = Point(randint(10, 19), randint(10, 19))
    rectangle = Rectangle(lower_left, top_right)

    print("Rectangle coordinates:")

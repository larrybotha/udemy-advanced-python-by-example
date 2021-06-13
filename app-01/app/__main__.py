import sys
from random import randint
from turtle import Turtle

from app.lib.geometry import GeometryCanvas, Point, Rectangle


def main():
    lower_left = Point(randint(0, 99), randint(0, 99))
    top_right = Point(randint(100, 199), randint(100, 199))
    rectangle = Rectangle(lower_left, top_right)

    print(f"Rectangle coordinates:\n{rectangle}\n")

    user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
    is_correct = rectangle.contains_point(user_point)
    point_messages = ["is", "" if is_correct else "not", "in the rectangle"]
    point_message = " ".join(filter(bool, point_messages))

    print(f"\n{user_point} {point_message}")

    user_area = input("\nWhat is the area: ")
    area = rectangle.area()
    area_answer_text = "correct" if user_area == area else "incorrect"

    print(f"\n{area_answer_text}! Rectange area is {area}")

    canvas = GeometryCanvas(Turtle())
    canvas.draw(rectangle, user_point)


if __name__ == "__main__":
    sys.exit(main())

from random import randint

from geometry import Point, Rectangle

if __name__ == "__main__":
    lower_left = Point(randint(0, 9), randint(0, 9))
    top_right = Point(randint(10, 19), randint(10, 19))
    rectangle = Rectangle(lower_left, top_right)

    print(f"Rectangle coordinates:\n{rectangle}\n")

    user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
    is_correct = rectangle.contains_point(user_point)
    answer_text = "" if is_correct else "not"

    print(f"\n{user_point} is {answer_text} in the retangle")

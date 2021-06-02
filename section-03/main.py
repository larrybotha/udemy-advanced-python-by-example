from typing import Type


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(
        self,
        lower_left: Type[Point],
        upper_right: Type[Point],
    ):
        lower_x, lower_y = lower_left
        upper_x, upper_y = upper_right

        if lower_x < self.x < upper_x and lower_y < self.y < upper_y:
            return True
        else:
            return False

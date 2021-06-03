"""geometry"""

from __future__ import annotations

from math import pow, sqrt


class Point:
    """Point."""

    def __init__(self, x, y):
        """__init__.

        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def distance_from_point(self, point: Point):
        """distance_from_point.

        :param point:
        :type point: Point
        """
        x, y = self
        xa, ya = point

        return sqrt(pow(xa - x, 2) + pow(ya - y, 2))

    def __iter__(self):
        """__iter__."""
        return iter([self.x, self.y])


class Rectangle:
    """Rectangle."""

    def __init__(self, point_bottom_left: Point, point_top_right: Point):
        """__init__.

        :param point_bottom_left:
        :type point_bottom_left: Point
        :param point_top_right:
        :type point_top_right: Point
        """
        self.bottom_left = point_bottom_left
        self.top_right = point_top_right

    def contains_point(self, point: Point) -> bool:
        lower_left, upper_right = self
        lower_x, lower_y = lower_left
        upper_x, upper_y = upper_right

        if lower_x < point.x < upper_x and lower_y < point.y < upper_y:
            return True
        else:
            return False

    def __iter__(self):
        return iter([self.bottom_left, self.top_right])

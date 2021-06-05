"""geometry"""

from __future__ import annotations

import turtle
from math import pow, sqrt
from turtle import Turtle


class Point:
    """Point."""

    def __init__(self, x: float, y: float):
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

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


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

        if lower_x <= point.x <= upper_x and lower_y <= point.y <= upper_y:
            return True
        else:
            return False

    def area(self):
        lower_left, upper_right = self
        lower_x, lower_y = lower_left
        upper_x, upper_y = upper_right

        return abs(upper_x - lower_x) * abs(upper_y - lower_y)

    def __iter__(self):
        return iter([self.bottom_left, self.top_right])

    def __repr__(self):
        return f"Rectangle(\n\t{self.bottom_left},\n\t{self.top_right}\n)"


class GeometryCanvas:
    # private member
    __canvas = None

    def __init__(self, canvas: Turtle):
        self.__canvas = canvas
        self.__canvas.speed(2)

    def draw(self, rectangle: Rectangle, point: Point):
        self.__draw_rectangle(rectangle)
        self.__draw_dot(point)
        turtle.done()

    def __draw_rectangle(self, rectangle: Rectangle):
        canvas = self.__canvas
        lower_left, upper_right = rectangle
        xa, ya = lower_left
        xb, yb = upper_right
        width = abs(xb - xa)
        height = abs(yb - ya)
        canvas.penup()
        canvas.goto(xa, ya)

        canvas.pendown()
        canvas.forward(width)
        canvas.left(90)
        canvas.forward(height)
        canvas.left(90)
        canvas.forward(width)
        canvas.left(90)
        canvas.forward(height)

    def __draw_dot(self, point: Point):
        canvas = self.__canvas
        canvas.penup()
        canvas.goto(point.x, point.y)
        canvas.pendown()
        canvas.dot()

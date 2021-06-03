# Section 3 - Creating and using Python classes

- `cls.__file__` returns the file where a class is defined
  ```python
  import os

  print(os.__file__)
  ```
- `str.count` returns the number of instances of a character in a string

  ```python
  "quick brown".count("quick")
  # 1
  ```
- `__iter__` can be used to make a class iterable, and thus support unpacking:

  ```python
  class Point:
      __init__(self, x, y):
        self.x = x
        self. y = y

      __init(self):
        return iter([x, y])

  p = Point(1,2)
  x, y = p
  # x = 1
  # y = 2
  ```

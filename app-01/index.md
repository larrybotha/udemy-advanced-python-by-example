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
- the ternary operator takes the following form in Python:

  ```python
  x if some_condition else y
  ```
- `input` values can be nested in class instantiations:

  ```python
  point = Point(float(input("x: ")), float(input("y: ")))
  ```

  - `input` returns a `str`, so we need to explicitly cast it to the correct
    type
- `MyClass` can be extended by providing it as an argument to another class:

  ```python
  class MyClass:
    # ...

  class MySubClass(MyClass):
    # ...
  ```

  - `MySubClass` _extends_ MyClass. _Subclassing_ is another name for extending
    a class
  - `MySubClass` is the child, while `MyClass` is the parent
- to make a class member or method private in Python, prepend with `__`:

  ```python
  class MyClass:
    __private_member = None

    def __init__(self):
      __private_member = 'something private'

    def __my_private_method(self):
      # ...
  ```
- protected members and methods in Python are prepended with a single underscore

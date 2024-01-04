#!/usr/bin/python3
"""
defining a Rectangle class
"""


class Rectangle:
    "Representative Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize Rectangle"""
        self.width = width  # Set width using the property setter
        self.height = height  # Set height using the property setter

    @property
    def width(self):
        """Getter method to retrieve the width attribute."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter method to set the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter method to retrieve the height attribute."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter method to set the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculate and return the rectangle area."""
        return self._width * self._height

    def perimeter(self):
        """Calculate and return the rectangle perimeter."""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self._width == 0 or self._height == 0:
            return ""
        rectangle = ""
        for _ in range(self._height):
            rectangle += "#" * self._width + "\n"
        return rectangle.rstrip()

    def __repr__(self):
        """Return a string representation that
        can be used to recreate the object."""
        return f"Rectangle(width={self._width}, height={self._height})"

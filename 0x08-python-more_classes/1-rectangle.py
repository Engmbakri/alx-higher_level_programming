#!/usr/bin/python3
"""
define Rectangle class
"""


class Rectangle:
    """Representative of Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle"""
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

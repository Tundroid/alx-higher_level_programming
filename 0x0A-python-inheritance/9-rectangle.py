#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a Rectangle"""

    def __init__(self, width, height):
        """Initializes object

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[{str(self.__class__.__name__)}] {self.__width}/{self.__height}"

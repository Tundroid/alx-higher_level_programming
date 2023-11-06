#!/usr/bin/python3
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

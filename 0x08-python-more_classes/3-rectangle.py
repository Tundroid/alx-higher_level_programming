#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        if type(width) is int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

        if type(height) is int:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

    @property
    def width(self):
        """Property to get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property to set width"""
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """Property to get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property to set height"""
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        s = ''
        if not self.width or not self.height:
            return s
        for i in range(self.height):
            s += '#' * self.width
            if i != self.height - 1:
                s += '\n'
        return s

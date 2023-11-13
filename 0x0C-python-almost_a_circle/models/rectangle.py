#!/usr/bin/python3
"""Rectanlge Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def validateWH(self, var, val):
        """Validate width and height"""
        if type(val) is int:
            if val > 0:
                return val
            raise ValueError(f"{var} must be > 0")
        raise TypeError(f"{var} must be an integer")

    def validateXY(self, var, val):
        """Validate X and Y"""
        if type(val) is int:
            if val >= 0:
                return val
            raise ValueError(f"{var} must be >= 0")
        raise TypeError(f"{var} must be an integer")

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        super().__init__(id)
        self.__width = self.validateWH("width", width)
        self.__height = self.validateWH("height", height)
        self.__x = self.validateXY("x", x)
        self.__y = self.validateXY("y", y)

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = self.validateWH("width", width)

    @property
    def height(self):
        """Gets the width"""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = self.validateWH("height", height)

    @property
    def x(self):
        """Gets the width"""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = self.validateXY("x", x)

    @property
    def y(self):
        """Gets the width"""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = self.validateXY("y", y)

    def area(self):
        """Gets the width"""
        return self.height * self.width

    def display(self):
        """Display polygon"""
        s = ''
        s += '\n' * self.y
        for i in range(self.height):
            s += ' ' * self.x
            s += '#' * self.width
            if i != self.height - 1:
                s += '\n'
        print(s)

    def __str__(self):
        """Modify str"""
        return "[{}] ({}) {}/{} - {}/{}".format(
                                                self.__class__.__name__,
                                                self.id,
                                                self.x, self.y, self.width,
                                                self.height
                                            )

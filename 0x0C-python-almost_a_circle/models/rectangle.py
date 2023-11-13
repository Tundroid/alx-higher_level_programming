#!/usr/bin/python3
"""Rectanlge Class"""
from models import base


class Rectangle(base.Base):
    """Rectangle Class"""
    def validateWH(self, var, val):
        if type(val) is int:
            if val > 0:
                return val
            raise ValueError(f"{var} must be > 0")
        raise TypeError(f"{var} must be an integer")

    def validateXY(self, var, val):
        if type(val) is int:
            if val >= 0:
                return val
            raise ValueError(f"{var} must be >= 0")
        raise TypeError(f"{var} must be an integer")

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = self.validateWH("width", width)
        self.__height = self.validateWH("height", height)
        self.__x = self.validateXY("x", x)
        self.__y = self.validateXY("y", y)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = self.validateWH("width", width)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = self.validateWH("height", height)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = self.validateXY("x", x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = self.validateXY("y", y)

    def area(self):
        return self.height * self.width

    def display(self):
        s = ''
        s += '\n' * self.y
        for i in range(self.height):
            s += ' ' * self.x
            s += '#' * self.width
            if i != self.height - 1:
                s += '\n'
        print(s)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
                                                self.__class__.__name__,
                                                self.id,
                                                self.x, self.y, self.width,
                                                self.height
                                            )

    def update(self, *args, **kwargs):
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.width = args[1] if len(args) > 1 else self.width
            self.height = args[2] if len(args) > 2 else self.height
            self.x = args[3] if len(args) > 3 else self.x
            self.y = args[4] if len(args) > 4 else self.y

        if kwargs:
            keys = set(kwargs.keys())
            self.id = kwargs["id"] if "id" in keys else self.id
            self.width = kwargs["width"] if "width" in keys else self.width
            self.height = kwargs["height"] if "height" in keys else self.height
            self.x = kwargs["x"] if "x" in keys else self.x
            self.y = kwargs["y"] if "y" in keys else self.y

    def to_dictionary(self):
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}

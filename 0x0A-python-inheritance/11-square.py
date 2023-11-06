#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size):
        """Initializes object

        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""


class MyInt(int):
    """Represents a Square"""

    def __init__(self, n):
        super().__init__()

    def __eq__(self, other):
        res = False
        if isinstance(other, MyInt):
            res = super().__ne__(other)
        return res

    def __ne__(self, other):
        res = True
        if isinstance(other, MyInt):
            res = super().__eq__(other)
        return res

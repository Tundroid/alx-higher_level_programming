#!/usr/bin/python3
"""Define a MyList class."""


class MyList(list):
    """Blueprint a MyList inheriting from list."""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        print(sorted(self))

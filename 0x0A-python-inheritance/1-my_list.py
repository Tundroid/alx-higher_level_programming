#!/usr/bin/python3
"""Define a MyList class."""


class MyList(list):
    """Blueprint a MyList inheriting from list."""

    def print_sorted(self):
        tmp = self.copy()
        tmp.sort()
        print(tmp)

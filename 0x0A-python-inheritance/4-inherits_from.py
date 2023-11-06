#!/usr/bin/python3
"""Defines a function to check for instance."""


def inherits_from(obj, a_class):
    """Return an object's methods and attribs.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False

#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return an object's methods and attribs."""
    return dir(obj)

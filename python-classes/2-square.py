#!/usr/bin/python3
"""A module for square"""


class Square:
    """Represent a square."""
    def __init__(self, size):
        """constructor for class properties"""
        if not isinstance(size, int)
            raise TyperError("size should be an integer")
        elif size < 0:
            raise ValuerError("the size should be greater than zero")
        self.__size = size

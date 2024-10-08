#!/usr/bin/python3
"""Working with OOP in python"""


class Square():
    """Implementing the square class"""
    def __init__(self, size=0):
        """ initialize the class
        Args:
           size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0 ")
        else:
            self.__size = size


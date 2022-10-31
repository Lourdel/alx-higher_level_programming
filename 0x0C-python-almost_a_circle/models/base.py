#!/usr/bin/python3
"""This module contains the base class of this project"""


class Base:
    """
    Definition of the base class and
    declaration of a class instance attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor method"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

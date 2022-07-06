#!/usr/bin/python3
"""
    1-my_list: class MyList
"""


class MyList(list):
    """
        MyList is a class that inherits from the list object
        Attributes:
            __init__: initializes the class instance
        Methods:
            print_sorted: prints a list in ascending format
            Returns: a sorted list in ascending form
    """
    def __init__(self):
        """
            __init__ initialises the class
            Args:
                self: the instance referring to the class
        """
        list.__init__(self)
    def print_sorted(self):
        """
            print_sorted prints a sorted list
            Args:
                self: argument that refers to the class
                Returns: sorted list
        """
        print(sorted(self))

#!/usr/bin/python3
class Base:
    """
        base creates a base model
        Attributes:
            __nb_objects: private variable
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializes the instance"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        
        

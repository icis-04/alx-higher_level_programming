#!/usr/bin/python3
import json
"""
    3-to_json_string: to_json_string()
"""
def to_json_string(my_obj):
    """
        to_json_string retuens json representation of an object
        Args:
            my_obj (str): the string to converted to json object
        Returns: JSON representation of an object (string)
    """
    return json.dumps(my_obj)


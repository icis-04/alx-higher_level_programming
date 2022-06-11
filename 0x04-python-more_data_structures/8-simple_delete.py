#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in a_dictionary.keys():
        if a_dictionary[key] == i:
            del a_dictionary[key]
        else:
            return a_dictionary
        return

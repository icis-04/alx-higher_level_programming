#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(0, len(my_list) - 1):
        i = idx
        if i < 0:
            return my_list
        elif i >= len(my_list):
            return my_list
        elif i == idx:
            return my_list.insert(idx, element)
    return

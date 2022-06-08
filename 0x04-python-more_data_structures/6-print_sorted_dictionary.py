#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dict = sorted(a_dictionary.keys())
    for i in b_dict:
        print(str(i) + ":",  a_dictionary[i])
    return

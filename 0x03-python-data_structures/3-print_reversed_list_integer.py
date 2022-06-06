#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse_list = list(my_list.reverse())
    for i in reverse_list:
        print(f'{i:d}')

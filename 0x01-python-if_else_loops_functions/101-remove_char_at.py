#!/usr/bin/python3
def remove_char_at(str, n):
    new_character = " "
    str = str[:n] + new_character + str[n+1:]
    return str

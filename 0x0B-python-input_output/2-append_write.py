#!/usr/bin/python3
"""
    2-append_write: appem=nd_write()
"""
def append_write(filename="", text=""):
    """
        append_file appends a string to a text file
        Args:
            filename (str): nmae of file
            text (str): text to be appended
        Returns: number of bytes written
    """
    with open(filename, 'a+', encoding='utf-8') as f:
        return f.write(text)

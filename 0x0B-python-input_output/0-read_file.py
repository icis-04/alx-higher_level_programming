#!/usr/bin/python3
"""
    0-read_file: read_file()
"""
def read_file(filename=""):
    """
        Returns string in a file.
        Args:
            filename(object): string.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")

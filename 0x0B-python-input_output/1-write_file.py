#!/usr/bin/python3
"""
    1-write_file: write_file()
"""
def write_file(filename="", text=""):
    """
        Returns the text as a string in the file
        Args:
            filename(object): string
            text(object): string
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)

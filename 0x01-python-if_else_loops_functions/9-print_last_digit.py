#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = number * -1
        number = num % 10
    else:
        number = number % 10
    print(number, end='')

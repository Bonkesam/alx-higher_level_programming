#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        mod  = number % 10
    else:
        mod = (number % 10) -10

    return (mod)

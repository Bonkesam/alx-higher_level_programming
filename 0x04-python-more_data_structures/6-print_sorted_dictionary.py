#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    my_keys = list(a_dictionary.keys())

    my_keys.sort()
    sorted__dict = {i: a_dictionary[i] for i in my_keys}
    return (sorted__dict)

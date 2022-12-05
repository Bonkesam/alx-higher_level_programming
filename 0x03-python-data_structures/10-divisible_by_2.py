#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    mat = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mat.append(True)
        else:
            mat.append(False)
    return mat

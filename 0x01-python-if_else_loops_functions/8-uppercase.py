#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123) and i != str[-1]:
            print("{}".format(chr(ord(i)-32)), end='')
        else:
            print("{}".format(i))

#!/usr/bin/python3
"""Define a clas square"""

class Square:
    """Represent a square"""
    def __init__(self, size):
	"""Initialize a square
	
	Args:
	   size(int): The size of the new intager

	"""
	if not isinstance(size, int):
		raise TypeError("size must be an intager")
	elif size < 0:
		raise ValueError("size must be >= 0")
	self.__size = size
    def area(self):
	"""Returns the area of the square"""
	return (self.__size * self.__size)

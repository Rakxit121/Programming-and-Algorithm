# Write a Python program to create the colon of a tuple.

from copy import deepcopy  # imported deepcopy

tup = (7, 8, 4, 5, 11, 78, 47, 55, 122, 178, 999, 456, 985)
print("Original Tuple : ", tup)
tup_copy = deepcopy(tup)
print("Colon of Tuple: ", tup_copy)

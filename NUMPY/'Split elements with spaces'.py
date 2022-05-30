# Write a NumPy program to split the element of a given array with spaces.

import numpy as np
x = np.array(['Python PHP Java C++'], dtype=np.str)
print("Original Array:")
print(x)
r = np.char.split(x)
print("\nSplit the element of the said array with spaces: ")
print(r)

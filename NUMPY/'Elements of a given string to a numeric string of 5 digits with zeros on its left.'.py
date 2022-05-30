# Write a NumPy program to make all the elements of a given string to a numeric string of 5 digits with zeros on its left. 


import numpy as np
x = np.array(['2', '11', '234', '1234', '12345'], dtype=np.str)
print("\nOriginal Array:")
print(x)
r = np.char.zfill(x, 5)
print("\nNumeric string of 5 digits with zeros:")
print(r)

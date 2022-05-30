# Write a NumPy program to repeat all the elements N times of a given array of string.

import numpy as np
x1 = np.array(['Python', 'PHP', 'Java', 'C++'], dtype=np.str)
print("Original Array:")
print(x1)
N = int(input("Enter the times that you want to repeat :- ")) 
new_array = np.char.multiply(x1, N)
print("New array:")
print(new_array)

# ELEMENT-WISE ARRAY MULTIPLICATION

""" Create a 3-by-3 array containing the even integers from 2 through 18. 
Create a second 3-by-3 array containing the integers from 9 down to 1, 
then multiply the first array by the second."""

import numpy as np

#1
result1 = np.arange(2, 19, 2).reshape(3, 3)

#2
result2 = np.arange(9, 0, -1).reshape(3, 3)

#3
result3 = result1 * result2

print(result1)
print(result2)
print(result3)
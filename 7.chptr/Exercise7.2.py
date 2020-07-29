# BROADCASTING
"""
Use arange to create a 2-by-2 array containing the numbers 0–3. 
Use broadcasting to perform each of the following operations on the original array:

Cube every element of the array.
Add 7 to every element of the array.
Multiply every element of the array by 2.
"""
import numpy as np

result = np.array([[0,1],[2,3]])

print(result)

print(result**3)
print(result + 7)
print(result**2)

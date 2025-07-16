# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

# Expected Output:

# Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]


import numpy as np

l=[12.23, 13.32,  100, 36.32]

arr1=np.array(l)

print(arr1)

# Create 3x3 Matrix (2?10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# Expected Output:

import numpy as np
li=list(range(2,11))

# [[ 2 3 4] [ 5 6 7] [ 8 9 10]]

arr1=np.array(li)

shaped=arr1.reshape(3,3)
print(shaped)


# 3. Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

a=np.zeros((10))

cnt=0


for i in range(len(a)):
    cnt+=1
    if cnt==6:
        a[5]=11

print(a)


# 4. Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.

# Expected Output:

# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

import numpy as np 

a=np.arange(12,38,1)
print(a)

# 5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.

# Sample output:

# Original array [1, 2, 3, 4]
import numpy as np
a=[1, 2, 3, 4]
arr=np.array(a)
print(arr)

b=np.astype(arr,float)
print(b)


# # 6. Celsius to Fahrenheit Conversion
# # Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. 
# # Centigrade values are stored in a NumPy array.

# # Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

# # Expected Output:

# # Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]

# # Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]


import numpy as np


celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])


fahrenheit = (celsius * 1.8) + 32


print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)


# Optional: Pretty print each pair
print("\nFormatted Conversion Table:")
for c, f in zip(celsius, fahrenheit):
    print(f"{c:.2f}°C = {f:.2f}°F")


# # 7. Append Values to Array (Do self-tudy)
# # Write a NumPy program to append values to the end of an array.

# # Expected Output:

# # Original array: [10, 20, 30]

# # After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

l=[10, 20, 30]

import numpy as np

arr=np.array(l)

# for i in range(40,100):
#     if i%10==0:
#         l.append(i)
#         arr=np.array(l)
# print(arr)

print(arr)

ranging=np.arange(40,100,10)

ft=np.append(arr,ranging)

print(ft)



# 8. Array Statistical Functions (Do self-tudy)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

import numpy 
a=numpy.random.randn(10)

print('\n',a)

mean=numpy.mean(a)
median=numpy.median(a)
std=numpy.std(a)

print('\nmean is',mean)
print('\nmedian is',median)
print('\nstd is',std)


# 9 Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.

import numpy 
a=numpy.random.randn(10,10)
print(a)

maxim=numpy.max(a)
print('\nmax value is-',maxim)

minum=numpy.min(a)
print('\nmin value is-',minum)


# 10
# Create a 3x3x3 array with random values.

import numpy 
matrix=numpy.random.randn(3,3,3)

print(matrix)





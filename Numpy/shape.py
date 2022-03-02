

# %%
## The number of dimensions an array has
import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

arr.ndim


# %%
##  The number of elements stored along each dimension of the array
import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

arr.shape


# %%
# Total number of array elements 
import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

arr.size


# %%
## Reshaping an array

import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

b = arr.reshape(9,1)

print(b)


# %%

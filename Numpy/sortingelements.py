

# %%
## Sorting arrays into ascending order

import numpy as np

arr = np.array([2,5,3,7,5,9,8,7,6,3,7,3,100])
np.sort(arr)

print(arr) ## This will eliminate commas in the printed array


# %%
## To concatenate individual arrays

import numpy as np


a = np.array([1,3,5])
x = np.array([7,9,11])

z = np.concatenate((a,x)) 

print(z)


# %%
## 
import numpy as np

a = np.array([[1,2,3], [4,5,6]])
b = np.array([[7,8,9]])

x = np.concatenate((a,b),axis=0)

print(x)


# %%
## 
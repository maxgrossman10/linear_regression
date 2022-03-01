# %%
## Creating a nested array 

import numpy as np

a = np.array([[1, 2, 3],[4, 5, 6]])
print (a[0])


# %%
## Creating an array with 6 zeros

import numpy as np

a = np.zeros(6)
print (a)


# %%
## Creating an array with only ones

import numpy as np

a = np.ones(11)
print (a)


# %%
## Creating an ascending array

import numpy as np

a = np.arange(45)
print (a)


# %%
## Creating an ascending array listing the (1st number, last, step size)

import numpy as np

a = np.arange(45, 100, 5)
print(a)


# %%
## An array with set range and where the NUMBER of steps is specified,
#  not the interval step size

import numpy as np

a = np.linspace(0,10, num=15)
print(a)
# %%

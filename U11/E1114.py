import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([2,3,4,5])
mse = np.mean((arr1 - arr2) ** 2)
print(mse)

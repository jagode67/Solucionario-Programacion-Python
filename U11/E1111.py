import numpy as np
arr = np.array([10, 20, 30, 40, 50])
arr[:] = np.mean(arr)
print(arr)

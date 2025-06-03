import numpy as np
A = np.random.uniform(-np.pi, np.pi, (50,50))
B = np.where(A < 0, -1, 1)
print(B)

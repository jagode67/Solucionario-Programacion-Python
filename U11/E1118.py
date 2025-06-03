import numpy as np
A = np.random.randint(0, 10, (4,4))
is_symmetric = np.allclose(A, A.T)
print("Matriz:\n", A)
print("¿Es simétrica?:", is_symmetric)

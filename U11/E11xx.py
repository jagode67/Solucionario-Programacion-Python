import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6]])
# Dividir en tres partes horizontales
result = np.hsplit(array, 3)
print(result)# [array([[1],[4]]), array([[2],[5]]), array([[3],[6]])]

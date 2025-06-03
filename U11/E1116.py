import numpy as np
arr = np.random.random(10)
p5 = np.percentile(arr, 5)
p95 = np.percentile(arr, 95)
print("Percentil 5:", p5)
print("Percentil 95:", p95)

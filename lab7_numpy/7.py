import numpy as np

arr_1 = np.full((4, 1, 3), 1)
arr_2 = np.full((12, 1), 1)
arr_3 = np.multiply(arr_1, arr_2)

print(arr_3.shape)


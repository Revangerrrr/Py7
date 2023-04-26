import numpy as np

arr_1 = np.full((3, 4), 3)
arr_2 = np.random.randint(0, 10, size=(2, 4))
print("Number of elements in arr_1:", arr_1.size)
print("Number of elements in arr_2:", arr_2.size)
arr_0 = np.concatenate((arr_1, arr_2), axis=0)
arr_3 = np.array((1, 8, 6, 5, 8, 3))
arr_4 = arr_3 * 3 + 1
arr_5 = arr_3.reshape((2, 3))
min_arr_5 = np.min(arr_5, axis=1)
mean_arr_5 = np.mean(arr_5)
arr_6 = np.arange(11) ** 2
print(arr_6[1::2])
print(arr_6[::-1])
arr_6[1::2] = 2
if 49 in arr_6:
    print("49 is in array arr_6")
else:
    print("49 is not in array arr_6")
A = np.array([[2, -3, 5, 8], [-1, 6, -4, 0], [3, 7, -2, -9]])
B = A[A < 0]

import numpy as np


def solve(arr1, arr2):
    if np.linalg.det(arr1) == 0:
        return 'det = 0'
    else:
        return np.linalg.solve(arr1, arr2)


a = []
b = []

for i in range(1, 3):
    for j in range(1, 3):
        a.append(int(input(f'a({i}{j}) ')))

for i in range(1, 3):
    b.append(int(input(f'b({i}) ')))

print(solve(np.array(a).reshape(2, 2), np.array(b)))

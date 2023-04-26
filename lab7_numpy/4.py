import numpy as np

arr = np.linspace(-2 * np.pi, 2 * np.pi, 13)
result = np.sum(np.sin(arr) ** 2 + np.cos(arr) ** 2)
print(np.sin(arr) ** 2 + np.cos(arr) ** 2)
if np.all(result):
    print("В ответе только единицы")
else:
    print("В ответе есть другие числа")
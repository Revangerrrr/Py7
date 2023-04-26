import numpy as np


def make_field(size):
    field = np.zeros((size, size), dtype=np.int8)
    field[::2, 1::2] = 1
    field[1::2, ::2] = 1
    return field


field_10 = make_field(10)
print(field_10)

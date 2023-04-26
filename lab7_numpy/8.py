import numpy as np

n = 3
m = 4

a = np.random.rand(n, m)
b = np.random.rand(1, m)
c = np.random.rand(m, n)
d = np.random.rand(1, m)

c_tran = np.transpose(c)
print(5 * a * b + c_tran * d)

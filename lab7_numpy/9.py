import numpy as np

x = np.array([(-3, 4, 1), (4, 3, 1)])
y = np.array([10, 12])
i = np.eye(3)
lambd = 0.1
x_tran = np.transpose(x)
teta = np.linalg.inv(x_tran @ x + lambd * i) @ x_tran @ y
print(teta)

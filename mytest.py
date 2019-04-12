
import numpy as np

def f(x, y):
    return 10 * x + y

b = np.fromfunction(f,(5,4),dtype=int)
# c = np.ones(3)
# print c
# for i in range(3):
#     print 'hello'
print b
print b[2, :]


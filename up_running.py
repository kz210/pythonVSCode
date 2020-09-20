import sys
from os import rename
import numpy as np

print (sys.executable)
x = np.arange(10)
y = np.sin(x)
b = [num*num for num in x]
c = (num*num for num in x)
print(y)
print(type(c))

import numpy as np
import matplotlib.pyplot as plt
from q01 import linear_conv
from q02 import circular_conv
from q03 import linear_conv2

x = np.array([4,3,2,1])
y = np.array([1,0,-1,0])

z1 = linear_conv(x, y)
z2 = circular_conv(x, y)
z3 = linear_conv2(x, y)

fig = plt.figure()
fig.add_subplot(1,3,1)
plt.stem(z1)
plt.title('q01')
fig.add_subplot(1,3,2)
plt.stem(z2)
plt.title('q02')
fig.add_subplot(1,3,3)
plt.stem(z3)
plt.title('q03')

fig.savefig('q04_graph')
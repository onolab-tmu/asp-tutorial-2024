import numpy as np
import matplotlib.pyplot as plt

N = 10
x = np.zeros(N)
x[0] = 1

i = np.arange(N)
y = 0.2*x[i] + 0.2*x[i-1] + 0.2*x[i-2] + 0.2*x[i-3] + 0.2*x[i-4]

fig, ax = plt.subplots(2, 1, sharex=True)

ax[0].grid()
ax[1].grid()

ax[0].stem(x)
ax[1].stem(y)

plt.savefig('./skotsugi/chapter03/q05.png')

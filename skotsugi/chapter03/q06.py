import numpy as np
import matplotlib.pyplot as plt

N = 10
x = np.zeros(N)
x[0] = 1 # impulse

def y(i: int):
  if i < 0: return 0
  return 0.3*y(i-1) + 0.4*x[i]

i = np.arange(N)

result = [y(i) for i in range(N)]

fig, ax = plt.subplots(2, 1, sharex=True)

ax[0].grid()
ax[1].grid()

ax[0].stem(x)
ax[1].stem(result)

plt.savefig('./skotsugi/chapter03/q06.png')

import numpy as np
import matplotlib.pyplot as plt
from q07 import diff_equation
from q08 import freqz

# impulse
L = 10
x = np.zeros(L)
x[0] = 1
a = [0]
b = [0.2, 0.2, 0.2, 0.2, 0.2]

y = diff_equation(a, b, x)

fs = 16000
N = 400
f = np.arange(0, 1, 1 / N) * fs
w = 2 * np.pi * f / fs

result = freqz(w, a, b)

A = np.abs(result)
theta = np.angle(result)
theta[A < 10**-5] = 0

fig, ax = plt.subplots(1, 2)
ax[0].stem(A)
ax[1].stem(theta)
plt.savefig('./skotsugi/chapter03/q09.png')

import numpy as np
import matplotlib.pyplot as plt

def white_noise(s, sn):
    N = len(s)
    x = 2 * (np.random.rand(N)) - 1     # ホワイトノイズの作成

    sum_s = 0
    sum_x = 0
    for n in range(N):
        sum_s += s[n] * s[n]
        sum_x += x[n] * x[n]

    mul = pow(np.exp(-sn/10) * sum_s / sum_x, 0.5)
    x = x * mul

    # return x
    ans = s + x
    return ans

fs = 16000
time = 1
f = 440
t = np.arange(-20, fs * time) / fs      # 20サンプル分手前に作っておく
s = np.sin(2 * np.pi * f * t)
epsilon = white_noise(s[20::], 10)
x1 = s[20:] + epsilon
x2 = s[10:len(s) - 10] + epsilon
x3 = s[:len(s) - 20] + epsilon
x = np.array([x1, x2, x3])

fig = plt.figure()
plt.subplot(3, 1, 1)
plt.xlim([0.5, 0.51])
plt.plot(t[20:], x1)
plt.xlabel('time[s]')
plt.title("x1")
plt.subplot(3, 1, 2)
plt.xlim([0.5, 0.51])
plt.plot(t[10:len(s) - 10], x2)
plt.xlabel('time[s]')
plt.title("x2")
plt.subplot(3, 1, 3)
plt.xlim([0.5, 0.51])
plt.plot(t[:len(s) - 20], x3)
plt.xlabel('time[s]')
plt.title("x3")
plt.savefig("./yyamamoto/chapter05/q06_graph.png")




import numpy as np
import matplotlib.pyplot as plt
from q08 import beam_pattern, F

fs = 16000
M = 3
c = 334
ds = [0.02, 0.05, 0.1]
fig, ax = plt.subplots(1, 3)

for i, d in enumerate(ds):
    # ステアリングベクトル
    w = np.zeros((F, M), dtype=complex)
    tau = (np.arange(M) - (M - 1) / 2) * d / c / fs
    for f in range(F):
        w[f, :] = np.exp(-1j * 2 * np.pi * f * tau) / M

    # 直線状アレイ
    p = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])

    A = beam_pattern(w, p, fs)
    ax[i].imshow(A)

plt.tight_layout()
plt.savefig("./skotsugi/chapter05/q09.png")

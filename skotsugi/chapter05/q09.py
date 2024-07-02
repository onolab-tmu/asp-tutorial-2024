import numpy as np
import matplotlib.pyplot as plt
from q03 import array_manifold_vector
from q08 import beam_pattern, F

fs = 16000
M = 3
c = 334
ds = [0.02, 0.05, 0.1]
fig, ax = plt.subplots(1, 3)

for i, d in enumerate(ds):
    # ステアリングベクトル
    w = np.zeros((F, M), dtype=complex)
    for f in range(F):
        a_w = array_manifold_vector(p, 0, f)
        w[f, :] = np.conj(a_w) / M

    # 直線状アレイ
    p = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])

    ax[i].pcolormesh(*beam_pattern(w, p, fs))

plt.tight_layout()
plt.savefig("./skotsugi/chapter05/q09.png")

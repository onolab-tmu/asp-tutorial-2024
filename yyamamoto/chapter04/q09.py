import scipy
import numpy as np
import matplotlib.pyplot as plt
from q03 import stft
from q04 import Hamming

fs = 16000
t = np.arange(fs) / fs
chirp = scipy.signal.chirp(t, f0=100, t1=t[-1], f1=16000)

L = 50
S = 25
fig = plt.figure()
for i in range(1, 5):
    L = L * 2
    S = S * 2
    H = Hamming(L)
    chirp_stft = stft(L, S, H, chirp)

    # スペクトログラムの準備
    A = 20 * np.log10(np.abs(chirp_stft))
    P = np.angle(chirp_stft)

    A = A.T
    P = P.T
    fig.add_subplot(1, 4, i)
    plt.pcolormesh(np.log10(np.abs(chirp_stft) ** 2).T)
    plt.title("L=" + str(L) + ", S=" + str(S))

fig.savefig("./yyamamoto/chapter04/q09_graph.png")
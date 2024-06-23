import numpy as np
import matplotlib.pyplot as plt
from q04 import correlation_matrix

def zero_padding(L, S, x):
    N = len(x)
    length = L - S + N
    if length % S != 0:
        length += S - (length % S)
    length += L - S
    ans = np.zeros(length)
    ans[L-S:L-S+N] = x

    return ans

def split_frame(L, S, x):
    x_tilde = zero_padding(L, S, x)
    N = len(x_tilde)
    T = (N - L) // S + 1

    ans = np.zeros((T, L))
    for t in range(T):
        ans[t] = x_tilde[t*S:t*S+L]
    return ans

def stft(L, S, w, x):
    x_splited = split_frame(L, S, x)
    T = x_splited.shape[0]
    x_stft = np.zeros((T, L//2+1), dtype=complex)
    for t in range(T):
        x_splited[t] = x_splited[t] * w
    for t in range(T):
        x_stft[t] = np.fft.rfft(x_splited[t])
    return x_stft



fs = 16000  # サンプリング周波数 Hz
sec = 5       # 信号長 s

t = np.arange(0, sec, 1/fs) # サンプリング点の配列
white_noise1 = 2 * (np.random.rand(fs*sec)) - 1
white_noise2 = 2 * (np.random.rand(fs*sec)) - 1


L = 512
S = 256
w = np.hanning(L)

X1 = stft(L, S, w, white_noise1)
X2 = stft(L, S, w, white_noise2)
X = np.stack([X1, X2])
print(correlation_matrix(X)[100].real)

# 結果の確認
# [[0.05582635 0.05582635]
#  [0.05582635 0.05582635]]
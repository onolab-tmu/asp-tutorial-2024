import numpy as np
from q02 import split_frame

def stft(L, S, w, x):
    x_splited = split_frame(L, S, x)
    T = x_splited.shape[0]
    x_stft = np.zeros((T, L//2+1), dtype=complex)
    for t in range(T):
        x_splited[t] = x_splited[t] * w
    for t in range(T):
        x_stft[t] = np.fft.rfft(x_splited[t])
    return x_stft
    
# 動作確認
# x = np.arange(16)
# w = np.arange(5)
# print(stft(5, 3, w, x))
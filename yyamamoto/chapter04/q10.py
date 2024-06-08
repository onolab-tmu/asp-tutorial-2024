import numpy as np
import matplotlib.pyplot as plt
from q03 import stft
from q04 import Hamming

def convert_unit(X, fs, S):
    freqs = fs * np.arange(X.shape[1]) / X.shape[1]
    T = X.shape[0]
    seconds = np.arange(0, S*T, step=S) / fs
    return freqs, seconds

fs = 16000
f = 440
time = 0.1
L = 1000
S = 500
t = np.arange(fs * time) / fs
sin_wave = np.sin(2 * np.pi * f * t)

H = Hamming(L)
sin_stft = stft(L, S, H, sin_wave)

freqs, seconds = convert_unit(sin_stft, fs, S)
fig = plt.figure()
plt.pcolormesh(seconds, freqs, np.log10(np.abs(sin_stft) ** 2).T)
plt.title("Spectrogram")
fig.savefig("./yyamamoto/chapter04/q10_graph.png")
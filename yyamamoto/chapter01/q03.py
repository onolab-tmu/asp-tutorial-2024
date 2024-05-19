import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

A = 1       # 振幅
f = 440     # 周波数 Hz
sec = 3     # 信号長 s
fs = 16000  # サンプリング周波数 Hz

t = np.arange(0, sec, 1/fs) # サンプリング点の配列

y1 = A * np.sin(2*np.pi*f*t) # 正弦波1

f = 660
y2 = A * np.sin(2*np.pi*f*t) # 正弦波2

# 2つの正弦波を2chでもつ行列 (行ベクトルをつなげているため転置)
y = np.stack([y1, y2]).T

sf.write("q03_audio.wav", y, fs, subtype="PCM_16")

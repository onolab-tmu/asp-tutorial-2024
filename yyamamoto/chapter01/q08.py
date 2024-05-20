import numpy as np
import math
import soundfile as sf

def add_white_noise(s, sn):
    N = len(s)
    x = 2 * (np.random.rand(N)) - 1     # ホワイトノイズの作成

    sum_s = 0
    sum_x = 0
    for n in range(N):
        sum_s += s[n] * s[n]
        sum_x += x[n] * x[n]

    mul = pow(math.exp(-sn/10) * sum_s / sum_x, 0.5)
    x = x * mul

    # return x
    ans = s + x
    return ans


# 正弦波の作成
A = 1       # 振幅
f = 440     # 周波数 Hz
sec = 3     # 信号長 s
fs = 16000  # サンプリング周波数 Hz
t = np.arange(0, sec, 1/fs) # サンプリング点の配列
y = A * np.sin(2*np.pi*f*t) # 正弦波の値

y = add_white_noise(y, 6)

sf.write("q08_audio.wav", y, fs, subtype="PCM_16")
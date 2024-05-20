# WAV ファイルの作成（ステレオ）: 振幅 1, 周波数 660 Hz の正弦波をサンプリング周波数 16000 Hz で 3 秒分作成し，1.で作成した信号と合わせて 2ch の wav ファイルとして保存せよ．

import numpy as np
import soundfile as sf

A = 1    # 振幅
f1 = 440    # 周波数
f2 = 660
fs = 16000    # サンプリング周波数
t = np.linspace(0, 3, 3 * fs)    # 3秒分作成

# 信号作成
x = np.zeros((3 * fs, 2))
x[:,0] = A * np.sin( 2 * np.pi * f1 * t )
x[:,1] = A * np.sin( 2 * np.pi * f2 * t )

# 書き込み
sf.write("q03.wav", x, fs, subtype="PCM_16")
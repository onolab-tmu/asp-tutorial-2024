# WAV ファイルの作成（モノラル）: 1.で作成した正弦波を 16bit PCM フォーマットで wav ファイルとして保存せよ．

import numpy as np
import soundfile as sf

A = 1    # 振幅
f = 440    # 周波数
fs = 16000    # サンプリング周波数
t = np.linspace(0, 3, 3 * fs)    # 3秒分作成
x = A * np.sin(2 * np.pi * f * t)    # 変位

sf.write("q02.wav", x, fs, subtype="PCM_16")    # 書き込み
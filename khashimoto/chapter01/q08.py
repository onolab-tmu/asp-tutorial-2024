# SN 比を指定した信号の混合（確認）: 8.で実装した関数を用いて，6.と同様にホワイトノイズと正弦波の混合信号を作成し wav ファイルとして保存せよ．ただし，SN 比が 6dB となるようにすること．

import numpy as np
import soundfile as sf

def mix_wn(org_s, snr):
    sna = np.sqrt(1 / (10 ** (snr/10)))    # ホワイトノイズの振幅
    wn = 2 * sna * np.random.rand(np.size(org_s)) - sna    # ホワイトノイズ
    mix = org_s + wn    # ホワイトノイズを重畳した信号
    return mix

A = 1    # 振幅
f = 440    # 周波数
fs = 16000    # サンプリング周波数
t = np.linspace(0, 3, 3 * fs)    # 3秒分作成
x = A * np.sin(2 * np.pi * f * t)    # 1.で作成した正弦波

mix = mix_wn(x, 6)    # ホワイトノイズと正弦波の混合信号
sf.write("q08.wav", mix, fs, subtype="PCM_16")    # 書き込み
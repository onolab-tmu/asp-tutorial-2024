# SN 比を指定した信号の混合（実装）: SN 比を任意の値に設定できるようにホワイトノイズの振幅を調整する関数を実装せよ．元信号と所望の SN 比を入力として受け取り，ホワイトノイズを重畳した信号を出力すること．

import numpy as np

def mix_wn(org_s, snr):
    sna = np.sqrt(1 / (10 ** (snr/10)))    # ホワイトノイズの振幅
    wn = 2 * sna * np.random.rand(np.size(org_s)) - sna    # ホワイトノイズ
    mix = org_s + wn    # ホワイトノイズを重畳した信号
    return mix
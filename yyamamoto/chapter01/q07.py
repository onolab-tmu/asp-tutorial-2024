import numpy as np
import math

def SN_rate(s, x):
    N = len(s)
    sum_s = 0
    sum_x = 0
    for n in range(N):
        sum_s += s[n]*s[n]
        sum_x += x[n]*x[n]
    ans = 10 * (math.log(sum_s) - math.log(sum_x))
    return ans



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


# あっているか確かめる (上の関数をホワイトノイズを出力するものに変更して確認)
A = 53       # 振幅
f = 423     # 周波数 Hz
sec = 3     # 信号長 s
fs = 16000  # サンプリング周波数 Hz

t = np.arange(0, sec, 1/fs) # サンプリング点の配列
y = A * np.sin(2*np.pi*f*t) # 正弦波の値

white_noise = add_white_noise(y, 234.23)
print(SN_rate(y, white_noise))

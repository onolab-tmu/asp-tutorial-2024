import numpy as np

def zero_padding(L, S, x):
    N = len(x)
    length = 2 * (L - S) + N
    if length % S != 0:
        length += S - (length % S)
    ans = np.zeros(length)
    ans[L-S:L-S+N] = x

    return ans

# 動作確認
# x = np.arange(3)
# print(zero_padding(7, 5, x))
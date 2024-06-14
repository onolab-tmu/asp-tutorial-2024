import numpy as np

def zero_padding(L, S, x):
    N = len(x)
    length = L - S + N
    if length % S != 0:
        length += S - (length % S)
    length += L - S
    ans = np.zeros(length)
    ans[L-S:L-S+N] = x

    return ans

# 動作確認
# x = np.ones(5)
# print(zero_padding(4, 2, x))
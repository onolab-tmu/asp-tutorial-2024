import numpy as np
from q01 import zero_padding

def split_frame(L, S, x):
    x_tilde = zero_padding(L, S, x)
    N = len(x_tilde)
    T = (N - L) // S + 1

    ans = np.zeros((T, L))
    for t in range(T):
        ans[t] = x_tilde[t*S:t*S+L]
    return ans

# 動作確認
# x = np.arange(16)
# print(split_frame(5, 3, x))
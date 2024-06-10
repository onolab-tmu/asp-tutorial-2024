import numpy as np

def zero_padding(L: int, S: int, x):
  # エラー処理
  if L < S:
    raise Exception('Shift size must be smaller than window size.')

  # 出力信号長の算出
  N = len(x)
  M = L - S    # > 0
  A = N + M*2
  B = int(A / S) + 1 # 条件を満たす最小のSの倍数
  C = S * B

  # 出力信号
  tilde = np.zeros(C) # 全体をゼロ埋め
  tilde[M:M+N] = x

  return tilde

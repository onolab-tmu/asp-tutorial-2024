import numpy as np

def zero_padding(L: int, S: int, x):
  # エラー処理
  if L < S:
    raise Exception('Shift size must be smaller than window size.')

  # 出力信号長の算出
  N = len(x)
  M = L - S    # > 0
  A = N + M
  B = A // S + 1 # 条件を満たす最小のSの倍数
  C = S * B + M

  # 出力信号
  tilde = np.zeros(C) # 全体をゼロ埋め
  tilde[M:M+N] = x

  return tilde

if __name__ == "__main__":
  x = np.ones(5)
  print(x)
  print(zero_padding(4, 3,))
import numpy as np
def DFT(x):
    N = len(x)
    X = [0] * N
    for k in range(N):
        s=0
        for n in range(N): 
            a = ((-2j) * np.pi * k * n) / N
            s = s + x[n] * np.exp(a)
           
        X[k] = s
    return X

def IDFT(X):
    N = len(X)
    x = [0] * N
    for n in range(N):
        s=0
        for k in range(N):
            angle = (2j * np.pi * k * n) / N
            s = s + X[k] * np.exp(angle)
        x[n] =s/N
    return x

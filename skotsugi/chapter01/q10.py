import numpy as np

def dma(x, k):
  y = np.zeros(len(x))
  for i in range(len(x) - k):
    y[i] = np.mean(x[i:i+k])
  return y

if __name__ == "__main__":
  import soundfile as sf
  signal, fs = sf.read('./skotsugi/chapter01/q09.wav')

  dmaed = dma(signal, 5)

  sf.write("./skotsugi/chapter01/q10.wav", dmaed, 8000)

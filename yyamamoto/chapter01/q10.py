import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

data, samplerate = sf.read('q09_audio.wav')

filtered = data
for i in range(len(filtered) - 4):
    filtered[i] = (data[i]+data[i+1]+data[i+2]+data[i+3]+data[i+4])

t = np.arange(0, 6, 1/samplerate) # サンプリング点の配列

fig = plt.figure()
A1 = fig.add_subplot(1,2,1)
plt.plot(t, data, label='original')
plt.legend()
A2 = fig.add_subplot(1,2,2)
plt.plot(t, filtered, label='filtered')
plt.legend()
fig.savefig('q10_graph')

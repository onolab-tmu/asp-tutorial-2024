import numpy as np
import matplotlib.pyplot as plt
from q08 import frequency_response

a = [1]
b = [0.2, 0.2, 0.2, 0.2, 0.2]
# b = [0.33, 0.33, 0.33]
fs = 16000
N = 16000
w, H = frequency_response(a, b, fs)
w = w[:N]
H = H[:N]


plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(w / (2 * np.pi) * fs, np.abs(H))
plt.title("Frequency Response - No-recursion (Amplitude)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dB)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(w / (2 * np.pi) * fs, np.angle(H))
plt.title("Frequency Response - No-recursion (Phase)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.grid(True)

plt.tight_layout()
plt.show()

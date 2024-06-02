import numpy as np
import matplotlib.pyplot as plt
from q08 import frequency_response

a = [1]
b = [0.2, 0.2, 0.2, 0.2, 0.2]
fs = 16000
N = 1024
w, H = frequency_response(a, b, fs, N)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(w / (2 * np.pi) * fs, 20 * np.log10(np.abs(H)))
plt.title("Frequency Response - Non-recursive (Magnitude)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(w / (2 * np.pi) * fs, np.angle(H))
plt.title("Frequency Response - Non-recursive (Phase)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.grid(True)

plt.tight_layout()
plt.show()

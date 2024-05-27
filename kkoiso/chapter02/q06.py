import numpy as np
import matplotlib.pyplot as plt


a = 1.0
freq= 440 
samp_rate = 16000 
d = 3  

t = np.linspace(0, d, int(samp_rate * d), endpoint=False)


sin_wave = a * np.sin(2 * np.pi * freq * t)

X = np.fft.fft(sin_wave)

#振幅をデシベル表記
amplitude_spectrum = 20 * np.log10(np.abs(X))

# 位相スペクトルの計算
phase_spectrum = np.angle(X)

#小さい振幅の位相も取っていたため、意味不明な位相スペクトルが出ていたので修正
for i in range(len(phase_spectrum)):
    
    if  amplitude_spectrum[i] < 0.001:
        phase_spectrum[i] = 0

 

# 対応する周波数を計算
frequencies = np.fft.fftfreq(len(X), 1/samp_rate)


plt.figure(figsize=(12, 6))
# 振幅スペクトルのプロット
plt.subplot(2, 1, 1)
plt.plot(frequencies,amplitude_spectrum)
plt.title('Amplitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True)

# 位相スペクトルのプロット
plt.subplot(2, 1, 2)
plt.plot(frequencies, phase_spectrum)
plt.title('Phase Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')
plt.grid(True)

plt.tight_layout()
plt.show()
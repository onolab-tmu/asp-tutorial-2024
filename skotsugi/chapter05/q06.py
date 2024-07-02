import numpy as np

fs = 16000
sec = 1
A = 1
f = 440
snr = 10

# make sin wave
t = np.arange(fs * sec) / fs
signal = A * np.sin(2 * np.pi * f * t)
signal_length = len(signal)

# make noise
signal_power = np.mean(signal**2)
snr_linear: float = 10.0 ** (snr / 10.0)
noise_power = signal_power / snr_linear
noise = np.sqrt(noise_power) * np.random.normal(0, 1, size=signal_length)

# signalを2つ結合する，
signal_twice = np.concatenate([signal, signal])

x = np.array(
    [
        signal + noise,
        signal_twice[10 : signal_length + 10] + noise,
        signal_twice[20 : signal_length + 20] + noise,
    ]
)

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    for x_i in x:
        plt.plot(t, x_i)

    plt.xlim([0, 0.01])
    plt.savefig("./skotsugi/chapter05/q06.png")

import numpy as np
from q02 import make_sin_wave
from q04 import make_white_noise
from q06 import square_mean, sn_rate

def add_noise_to_signal(signal, snr):
  s_power = square_mean(signal)

  snr_linear = 10.0 ** (snr / 10.0)
  n_power = s_power / snr_linear

  noise = np.sqrt(n_power) * make_white_noise(len(signal))
  noisy_signal = signal + noise

  return noisy_signal, noise

##### DEBUG #####
if __name__ == "__main__":
  np.random.seed(0)

  fs = 16000
  sec = 3.0

  signal = make_sin_wave(1.0, 440, fs, sec)
  noisy_signal, noise = add_noise_to_signal(signal, 20)

  print(sn_rate(signal, noise))

import matplotlib.pyplot as plt

def show_spectrum(filename, amp, phs): 
  fig, axs = plt.subplots(1, 2)

  axs[0].stem(amp)
  axs[0].set_title('Amplitude')
  axs[1].stem(phs)
  axs[1].set_title('Phase')

  fig.tight_layout()

  plt.savefig(filename)

if __name__ == "__main__":
  import numpy as np
  from q01 import dft

  delta = [1, 0, 0, 0, 0, 0, 0, 0]
  d = dft(delta)

  amp = np.abs(d)
  phs = np.angle(d)

  show_spectrum('./skotsugi/chapter02/q04.png', amp, phs)
  
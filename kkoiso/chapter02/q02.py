import numpy as np
import matplotlib.pyplot as plt
from q01 import DFT,IDFT

x = np.array([1, 0, 0, 0, 0, 0, 0, 0])
X = DFT(x)


print(X)


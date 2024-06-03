import matplotlib.pyplot as plt
from q01 import linear_conv
from q02 import circular_conv
from q03 import circular_zero_conv

x = [4, 3, 2, 1]
y = [1, 0, -1, 0]

z_l = linear_conv(x, y)
z_c = circular_conv(x, y)
z_z = circular_zero_conv(x, y)

fig, ax = plt.subplots(3, 1, sharex=True, sharey=True)

ax[0].grid()
ax[1].grid()
ax[2].grid()

ax[0].stem(z_l.real)
ax[1].stem(z_c.real)
ax[2].stem(z_z.real)

plt.savefig('./skotsugi/chapter03/q04.png')
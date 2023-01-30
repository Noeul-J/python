import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import drawing_line as dl

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
fig.set_size_inches((15, 6))

ax1.xaxis.set_tick_params(labelsize=18)
ax1.yaxis.set_tick_params(labelsize=18)

x = np.linspace(-2, 2, 100)
a1, a2, a3 = 2, 3, 4
y1, y2, y3 = a1**x, a2**x, a3**x

ax1.plot(x, y1, color='k', label=r"2^x")
ax1.plot(x, y2, '--', color='k', label=r"3^x")
ax1.plot(x, y3, ':', color='k', label=r"4^x")

ax1.set_xlabel('x', fontsize=25)
ax1.set_ylabel('y', fontsize=25)
ax1.legend(fontsize=20)

ax2.xaxis.set_tick_params(labelsize=18)
ax2.yaxis.set_tick_params(labelsize=18)

x = np.linspace(-2, 2, 100)
a1, a2, a3 = 1/2, 1/3, 1/4
y1, y2, y3 = a1**x, a2**x, a3**x

ax2.plot(x, y1, color='k', label=r"(1/2)^x")
ax2.plot(x, y2, '--', color='k', label=r"(1/3)^x")
ax2.plot(x, y3, ':', color='k', label=r"(1/4)^x")

ax2.set_xlabel('x', fontsize=25)
ax2.set_ylabel('y', fontsize=25)
ax2.legend(fontsize=20)

dl.arrowed_spines(fig, ax1)
dl.arrowed_spines(fig, ax2)

plt.show()




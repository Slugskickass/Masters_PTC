import numpy as np
import matplotlib.pyplot as plt

signal = np.load('signal.npy')
noise = np.load('noise.npy')

plt.plot(signal, noise)


plt.savefig('line_plot.pdf')
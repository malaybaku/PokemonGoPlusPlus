# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    filename = "accels.csv"
    datas = np.loadtxt(filename, delimiter=",")

    x = datas[:,0]
    X = np.fft.fft(x)
    amplitudes = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
    freqs = np.fft.fftfreq(x.shape[0], d=1.0/200.0)

    subplot(211)
    plt.plot(ramge(x.shape[0]), x)
    plt.xlabel("time")
    plt.ylabel("amplitude")

    plt.subplot(212)
    plt.plot(freqs, amplitudes)
    plt.xlabel("freq[Hz]")
    plt.ylabel("amplitude")

    plt.show()
    
    

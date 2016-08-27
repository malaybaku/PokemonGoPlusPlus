# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    filename = "accels.csv"
    datas = np.loadtxt(filename, delimiter=",")

    #Accel X (Top graph)
    plt.subplot(311)
    plt.plot(datas[:,0])

    #Accel Y (Center graph)
    plt.subplot(312)
    plt.plot(datas[:,1])
    
    #Accel z (Bottom graph)
    plt.subplot(313)
    plt.plot(datas[:,2])

    plt.show()

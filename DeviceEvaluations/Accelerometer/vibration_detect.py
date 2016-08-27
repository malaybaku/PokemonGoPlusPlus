# -*- coding:utf-8 -*-

import time

from adxl345 import ADXL345, BW_RATE_200HZ

if __name__ == "__main__":
    adxl345 = ADXL345()
    adxl345.setBandwidthRate(BW_RATE_200HZ)
    #print "ADXL345 on address 0x%x:" % (adxl345.address)
    accels_x = []
    accels_y = []
    accels_z = []
    t1 = time.time()
    for _ in range(200):
        axes = adxl345.getAxes(True)
        accels_x.append(axes['x'])
        accels_y.append(axes['y'])
        accels_z.append(axes['z'])
        time.sleep(0.005)

    t2 = time.time()

    print("elapsed(sec): {0}".format(t2 -  t1))
    
    with open("accels.csv", "w") as f:
        for i in range(len(accels_x)):        
            f.write(",".join(str(v) for v in [accels_x[i], accels_y[i], accels_z[i]]) + "\n")

    

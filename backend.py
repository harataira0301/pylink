#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rf
#
# Created:     28/09/2014
# Copyright:   (c) rf 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import os
from scipy import signal
from matplotlib.pyplot import plot, legend, show, hold, grid, figure, savefig, xlim

def display_graph(standardization = 0):
    signal_names = []
    for dpath, dnames, fnames in os.walk("./data/"):
        for fname in fnames:
            if fname.endswith(".log"):
                signal_names.append(fname.replace(".log",""))

    print(signal_names)

    colors = ('r','b','g','r','b','g','r','b','g')

    i=0
    figure()
    for sn in signal_names:
        t,y = get_data_from_logfile("data/"+sn+".log",standardization)
        plot(t, y, 'k',color = colors[i], linewidth=1.75)
        i+=1
    legend((signal_names), loc='best')
    hold(False)
    grid(True)


def get_data_from_logfile(log_file,standardization = 0):
    t=[]
    y=[]
    log_file = open(log_file,"r")

    for line in log_file:
        new_t,new_y = line.rstrip().split(',')

        t.append(float(new_t))
        y.append(float(new_y))

    log_file.close()
    if standardization:
        y = y/np.max(y)
    return t,y

def main():
    display_graph(1)
    get_corr()
    pass

def get_corr():
    t,out_t = get_data_from_logfile("data/in.log",1)
    _,sinc_t = get_data_from_logfile("data/rtl_sinc.log",1)

    t2 = np.linspace(-np.max(t),np.max(t),len(t) * 2 - 1)
    cor = signal.correlate(out_t,sinc_t)

    log_file = open("data/cor.txt","w")
    i=0
    for c in cor:
        log_file.write(str(t2[i])+","+str(c)+"\n")
        i+=1

    #peakind = signal.find_peaks_cwt(cor,np.arange(1,2))

    figure()
    plot(t2, cor, 'k',color = 'b', linewidth=1.75)
    xlim(-4,4)
    legend("cross correlation", loc='best')
    hold(False)
    grid(True)
    show()

if __name__ == '__main__':
    main()
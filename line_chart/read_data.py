import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from pylab import *
import json
import os
import pdb
import csv
import pandas
def read_data_line(path):
    data = pandas.read_csv(path,sep="\t",header=None)
    return data

if __name__ == '__main__':
    data = read_data_line("../line_data.csv")
    data = data.cumsum()
    plt.figure(); data.plot(); plt.legend(loc='best')
    plt.show()

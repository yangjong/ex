import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rawdata = pd.read_csv("accel_4.txt", names=['x1_acc', 'y1_acc', 'z1_acc', 'x2_acc', 'y2_acc', 'z2_acc', 'x3_acc', 'y3_acc', 'z3_acc'])

rawdata.info()

del rawdata['x2_acc']
del rawdata['y2_acc']
del rawdata['z2_acc']
del rawdata['x3_acc']
del rawdata['y3_acc']
del rawdata['z3_acc']

rawdata.info()

rawdata.to_csv('rawdata_sesor5.txt',index=False)

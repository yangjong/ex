import pandas as pd
import matplotlib.pyplot as plt

rawdata = pd.read_csv('accel0.txt', names=['accx1','accy1','accz1','accx2','accy2','accz2','accx3','accy3','accz3'])
ts = 9.2 * 0.0000000001
i = 0
for i in range(379):
	rawdata['index'] = i
	rawdata['time'] = rawdata.index * ts

rawdata.plot(x='time', y='accx1', legend=False)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rawdata = pd.read_csv("sensor_zacc1_train.txt", names=['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','z','p','q','r','1','2','3','4','5','6','7','8','9','10','11','12','13'])


cols =['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','z','p','q','r','1','2','3','4','5','6','7','8','9','10','11','12','13']
rawdata[cols] = rawdata[cols].apply(np.float64)


rawdata.info()
rawdata.to_csv("sensor1_zacc1_train.txt", index=False)

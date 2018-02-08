import numpy as np
import pandas as pd

rawdata = pd.read_csv("sensor1_xacc1_test.txt", names=['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','z','p','q','r','1','2','3','4','5','6','7','8','9','10','11','12','13'])


cols =['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','z','p','q','r','1','2','3','4','5','6','7','8','9','10','11','12','13']


Minx=-32768
Maxx=32768

rawdata[cols] = 2 * ((rawdata[cols] - Minx) / (Maxx - Minx)) -1
rawdata.to_csv("sensor1_xacc_test.txt", index=False)

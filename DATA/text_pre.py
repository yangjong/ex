
f1 = open('rawdata_sesor1.txt', 'r')
f2 = open('rawdata1_sensor.txt','w')


for line in f1:
	f2.write(line.replace('', ',',1))

#for line in f2:
#	f1.write(line.replace(',', 'ForhendStroke, ', 1))

f1.close()
f2.close()


"""
counter = 0
with open("accel1_y1.txt") as f:
	for line in f:
		counter += len(line.split(","))
 		print conuter
"""

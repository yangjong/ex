
f1 = open('sensor_xacc1_test.txt', 'r')
f2 = open('sensor1_xacc1_test.txt','w')


for line in f1:
	f2.write(line.replace(',', '  '))

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

import csv

f1='accel_4.txt'
f2='accel5_y.txt'

with open(f1, 'r') as fin:
	with open(f2, 'w') as fout:
		writer = csv.writer(fout)
		for row in csv.reader(fin, delimiter=","):
			writer.writerow(row[1:2]) 




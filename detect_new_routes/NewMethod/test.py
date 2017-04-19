import random
import sys
import csv
import nltk.tokenize
import math

month_label = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
data = []
Files = ['2013-2016OD_TH_0.00']
for File in Files:

	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)
	ifile.close()

for i in data:
	print i

print data[1]
select = []
select.append(data[0])
select.append(data[1])
for i in data:
	if i[0] == "TG" and int(i[456]) > 1000 and i[2] == '':
		select.append(i)

print len(data)
print len(select)
print len(data[2])
print select[2][456]

b = open('TG_not.csv', 'w')
a = csv.writer(b,quoting=csv.QUOTE_ALL,lineterminator="\n")
a.writerows(select)
b.close()
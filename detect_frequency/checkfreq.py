import random	
import sys
import csv
import nltk.tokenize
import math
from numpy import arange,array,ones,linalg
from pylab import plot,show
import re

equipment = []
Files = ['sumation_3years']
data_cut = []
sumation = []
for File in Files:

	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		equipment.append(row)
	ifile.close()

#for i in equipment:
#	print i

output = []
output.append(equipment[0])
#for i in equipment:
#	if i[1] == "FD" and i[2] == "CNX" and i[3] == "DMK" :
#		output.append(i)

#for i in output:
#	print i

new_freq = []
no_new_freq = []
#print equipment[4][0][6]
#print equipment[0][1]
#print equipment[1][1]
#print equipment[2][1]

for i in range(1,len(equipment)):
	for j in range(i+1,len(equipment)):
		if equipment[i][1] == equipment[j][1] and equipment[i][2] == equipment[j][2] and equipment[i][3] == equipment[j][3]:
			if re.search(equipment[i][0][0:3],equipment[j][0]) and not(re.search("2016",equipment[j][0])):
				if float(equipment[i][4]) < float(equipment[j][4]) and int(equipment[j][0][6])-int(equipment[i][0][6])==1:
					#new_freq.append(equipment[i])
					new_freq.append(equipment[i])
#					print equipment[i]
#					print equipment[j]
#					print type(equipment[i][4])
#					print equipment[i][4]
#					print type(equipment[j][4])
#					print equipment[j][4]
#					print " "
					break
				elif float(equipment[i][4]) == float(equipment[j][4]) and int(equipment[j][0][6])-int(equipment[i][0][6])==1:
					no_new_freq.append(equipment[i])
					#print equipment[i]
					#print equipment[j]
				#	print type(equipment[i][4])
					#print equipment[i][4]
				#	print type(equipment[j][4])
					#print equipment[j][4]
					#print " "
 

#for i in no_new_freq:
#	print i
print len(no_new_freq)
print len(new_freq)						
b = open('yes.csv', 'w')
a = csv.writer(b,quoting=csv.QUOTE_ALL,lineterminator="\n")
a.writerows(new_freq)
b.close()	
b = open('no.csv', 'w')
a = csv.writer(b,quoting=csv.QUOTE_ALL,lineterminator="\n")
a.writerows(no_new_freq)
b.close()	

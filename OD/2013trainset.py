import random
import psycopg2
import sys
import csv
import nltk.tokenize
import math

month_label = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
data = []
Files = ['2013-2016OD_TH']
for File in Files:

	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)
	ifile.close()	

#select = ['CNX','BKK']
#for i in range(0,len(data)):
#	print str(i) + str(data[i][0])
#print len(data)

att = data[10];
length_column = 463
length_row = len(data)-23
#print length_row

fixed_att = [0,22]
split_att = [23,28]
	
#for i in range(len(data)-25,len(data)-23):
#	print data[i]
data_cut = []
print data[11][30]
print type(data[11][30])
#data_cut.append([data[10][0:23],data[10][24:29]])
#print data_cut
#data_cut.append(['month',att[0][15],att[0][16],att[0][17],att[0][18],att[0][19],att[0][20],att[0][22],att[0][24],att[0][26],att[0][27],att[0][28]])
#print data_cut
for i in range(11,length_row):
	j = 23
	k = 0
	count = 0
	while j+9 <= length_column :
		#if k == 37:
		#	data_cut.append([data[i][0:23],data[i][j+1:j+6],"total"])
		print data[i][j+8]
		if float(data[i][j+8]) != 0:
			data_cut.append([data[i][0:23],data[i][j:j+9],month_label[k%12]+str(2013+count)])
		if k%12 == 11:
			count+=1
		k+=1
		j+=9

#for i in range(1,10):
#	print data_cut[i]
#print len(data)
#print len(data_cut)
#print data[10]

#	if data[i][0][15] == origin:
#		if data[i][0][22] == dest:
#			data_cut.append([data[i][1],data[i][0][15],data[i][0][16],data[i][0][17],data[i][0][18],data[i][0][19],data[i][0][20],data[i][0][22],math.log10(float(data[i][0][24].replace(',', ''))),math.log10(float(data[i][0][26].replace(',', ''))),math.log10(float(data[i][0][27].replace(',', ''))),math.log10(float(data[i][0][28].replace(',', '')))])
				#data[i][8],3

#data_cut.sort()	
#for i in range(len(data_cut)):
#	print data_cut[i]
	

b = open('test_2013.csv', 'w')
a = csv.writer(b,quoting=csv.QUOTE_ALL,lineterminator="\n")
a.writerows(data_cut)
b.close()		
#print data[1]

import random
#import psycopg2
import sys
import csv
import nltk.tokenize
import math
import numpy as np
from pylab import plot,show
import statsmodels.api as sm
from sklearn import preprocessing

def reg_m(y, x):
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results

def normalization(data):
    norm_data = []
    for i in range(0,len(data)):
        #print data[i]
        norm_data.append((data[i]-min(data))/(max(data)-min(data)))
    return norm_data

data = []
Files = ['3years']
for File in Files:

	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)
	ifile.close()

y = []
xi = []
#for i in range(0,len(data[0])):
#	print str(i)+ " " + data[0][i]

#for i in range(1,len(data)):
#	for j in data[i]:
#		pass
for i in range(1,len(data)):
	y.append(data[i][3])
	xi.append([float(data[i][4])*32,data[i][5],data[i][6],data[i][7],data[i][8],data[i][10],data[i][13],data[i][16]])
#	xi.append([math.log10(x[4]),math.log10(x[5]),math.log10(x[6]),math.log10(x[7]),math.log10(x[8]),math.log10(x[10]),math.log10(x[13])])

#for i in xi:
#	print i[0]
#	print type(i[0])

for x in range(0,len(y)):
	y[x] = math.log10(float(y[x]))

#print y
for x in range(0,len(xi)):
	for i in range(0,len(xi[x])):
		#print i
		xi[x][i] = math.log10(float(xi[x][i]))
		#print i

#print len(xi[0])
in_x = []
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
for i in range(0,len(xi)):
	x1.append(xi[i][0])
	x2.append(xi[i][1])
	x3.append(xi[i][2])
	x4.append(xi[i][3])
	x5.append(xi[i][4])
	x6.append(xi[i][5])
	x7.append(xi[i][6])
	x8.append(xi[i][7])
in_x.append(x1)
in_x.append(x2)
in_x.append(x3)
in_x.append(x4)
in_x.append(x5)
in_x.append(x6)
in_x.append(x7)
in_x.append(x8)

norm_in_x = []
for i in in_x:
	normx = normalization(i)
	norm_in_x.append(normx)

#in_x = preprocessing.normalize(in_x)
#print xi
#for i in xi:
#	print i
#y = [1,2,3,4,3,4,5,4,5,5,4,5,4,5,4,5,6,5,4,5,4,3,4]

#x = [
#     [4,2,3,4,5,4,5,6,7,4,8,9,8,8,6,6,5,5,5,5,5,5,5],
#     [4,1,2,3,4,5,6,7,5,8,7,8,7,8,7,8,7,7,7,7,7,6,5],
#     [4,1,2,5,6,7,8,9,7,8,7,8,7,7,7,7,7,7,6,6,4,4,4]
#     ]


print reg_m(y, in_x).summary()

print reg_m(y, norm_in_x).summary()
#print norm_in_x
import random
import sys
import csv
import nltk.tokenize
import math
import numpy as np
from pylab import plot,show
import statsmodels.api as sm
from sklearn import preprocessing
from scipy.stats.stats import pearsonr
import re
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = []
Files = ["index_n_route"]
for File in Files:
	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)
	ifile.close()
index = []
for i in data:
	index.append(i[0])
#print index

data = []
Files = ["income_pop_visitor_tourist"]
for File in Files:
	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)
	ifile.close()

out = []
#print data[1][0]
#print len(index)
for i in range(0,len(data)):
	#print i
	check = False
	for j in range(0,len(index)):
		#print i
		#print j
		if data[i][0] == index[j]:
			check = True
			break
	temp = []
	#print i
	for j in range(0,len(data[i])):
		temp.append(data[i][j])
	if check:
		temp.append(0)
	else:
		temp.append(1)
	#print temp
	out.append(temp)
	#print i
		
#for i in index:
#	for j in range(0,len(data)):
		#print data[j][0]
#		if i[0] == data[j][0]:
#			temp = []
#			for k in data[j]:
#				temp.append(k)
#			temp.append(0)
#			out.append(temp)
#for i in out:
#	print i

b = open('income_pop_visitor_tourist_log.csv', 'w')
a = csv.writer(b,quoting=csv.QUOTE_ALL,lineterminator="\n")
a.writerows(out)
b.close()
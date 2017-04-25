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
Files = ["new_freq_data_final"]
for File in Files:
	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)
	ifile.close()

yes = []
for i in range(1,len(data)):
	yes.append(data[i])

data = []
Files = ["no_new_freq_data_final"]
for File in Files:
	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)
	ifile.close()

no = []
for i in range(1,len(data)):
	no.append(data[i])

random.shuffle(yes)
random.shuffle(no)

out = []
for j in range(0,min(len(yes),len(no))-min(len(yes),len(no))%10):
	#print j
	temp = []
	for i in yes[j]:
		temp.append(i)
	temp.append(1)
	out.append(temp)
	temp2 = []
	for i in no[j]:
		temp2.append(i)
	temp2.append(0)
	out.append(temp2)

random.shuffle(out)
#for i in out:
#	print i
b = open('logistic_new_flightfreq_data.csv', 'w')
a = csv.writer(b,quoting=csv.QUOTE_ALL,lineterminator="\n")
a.writerows(out)
b.close()	
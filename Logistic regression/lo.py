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


def logistic(ytrain,xtrain,ytest,xtest):
	Ytrain = np.array(ytrain)
	Xtrain = np.array(xtrain)
	Ytest = np.array(ytest)
	Xtest = np.array(xtest)
	#a = np.array(x)
	#b = np.array(y)
	lr = LogisticRegression().fit(Xtrain,Ytrain)
	yhat = lr.predict(Xtest)

	#print b
	#print yhat
	print accuracy_score(Ytest, yhat)
	return accuracy_score(Ytest, yhat)

data = []
Files = ["logistic_data_no_SL"]
for File in Files:
	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)
	ifile.close()

random.shuffle(data)

x = []
y = []

for i in data:
	#x.append([float(i[7]),float(i[8]),float(i[10])])
	x.append([float(i[5]),float(i[6]),float(i[7]),float(i[8]),float(i[10])])
	y.append(i[11])

print len(x)
print len(y)

ytrain = y[0:34]
ytest = y[34:]
xtrain = x[0:34]
xtest = x[34:]

logistic(ytrain,xtrain,ytest,xtest)
	#acc.append(temp)
#print len(y)
#print y
#print y[0:8]
#print y[8:16]

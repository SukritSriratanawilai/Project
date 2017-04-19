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
Files = ["income_pop_visitor_tourist_log_2013"]
for File in Files:
	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)
	ifile.close()

#no = []
#yes = []
#for i in data:
#	if i[13] == 0:
#		no.append(i)
#	else:
#		yes.append(i)

#print yes
#print no

#random.shuffle(no)
random.shuffle(data)

x = []
y = []


for i in data:
	#x.append([float(i[7]),float(i[8]),float(i[10])])
	x.append([float(i[5]),float(i[6]),float(i[9]),float(i[12])])
	y.append(i[13])

#print y
acc = []
num_folds = 10
subset_size = 3

for i in range(num_folds):
	#print i
	y_testing_this_round = y[i*subset_size:(i+1)*subset_size]
	x_testing_this_round = x[i*subset_size:(i+1)*subset_size]
	y_training_this_round = []
	x_training_this_round = []
	for j in range(0,i*subset_size):
		y_training_this_round.append(y[j])
		x_training_this_round.append(x[j])
	for j in range((i+1)*(subset_size),len(y)):
		y_training_this_round.append(y[j])
		x_training_this_round.append(x[j])

	#print y_testing_this_round
	#print y_training_this_round
	#print y
	#print " "
	logistic(y_training_this_round,x_training_this_round,y_testing_this_round,x_testing_this_round)
	#acc.append(temp)
#print len(y)
#print y
#print y[0:8]
#print y[8:16]

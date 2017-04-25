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
from sklearn.metrics import precision_recall_fscore_support as score
def normalization(data):
    norm_data = []
    for i in range(0,len(data)):
        #print data[i]
        norm_data.append((data[i]-min(data))/(max(data)-min(data)))
    return norm_data


def CrossValidation(data):

	x = []
	y = []

	for i in data:
		x.append([float(i[4]),float(i[5]),float(i[6]),float(i[7]),float(i[8]),float(i[10]),float(i[16])])
		y.append(int(i[17]))

	norm_in_x = []
	x1 = []
	x2 = []
	x3 = []
	x4 = []
	x5 = []
	x6 = []
	x7 = []
	#x8 = []
	for i in range(0,len(x)):
		x1.append(x[i][0])
		x2.append(x[i][1])
		x3.append(x[i][2])
		x4.append(x[i][3])
		x5.append(x[i][4])
		x6.append(x[i][5])
		x7.append(x[i][6])
		#x8.append(x[i][7])
	#for i in range(len(x)):
	#	print x[i][0]
	#	print x1[i]

	n1 = normalization(x1)
	n2 = normalization(x2)
	n3 = normalization(x3)
	n4 = normalization(x4)
	n5 = normalization(x5)
	n6 = normalization(x6)
	n7 = normalization(x7)
	#n8 = normalization(x8)
	#print len(n1)
	#print n1
	x = []
	for i in range(len(n1)):
		x.append([n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i]])

	acc = []
	num_folds = 10
	subset_size = len(x)/10
	y_predict = []
	for i in range(num_folds):
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

		yhat = logistic(y_training_this_round,x_training_this_round,y_testing_this_round,x_testing_this_round)
		for k in yhat:
			y_predict.append(k)

	ytest = y[0:len(y_predict)]
	precision, recall, fscore, support = score(ytest, y_predict)

	print('precision: {}'.format(precision))
	print('recall:    {}'.format(recall))
	print('fscore:    {}'.format(fscore))
	print('support:   {}'.format(support))
	print accuracy_score(ytest, y_predict)
	#print ytest 
	#print y_predict
	t = [0,0,0,0]
	for i in range(0,len(ytest)):
		if ytest[i] == y_predict[i]:
			if ytest[i] == 1:
				t[0]=t[0]+1
			else:
				t[3]=t[3]+1
		else:
			if ytest[i] == 0 and y_predict[i] == 1:
				t[1]=t[1]+1
			if ytest[i] == 1 and y_predict[i] == 0:
				t[2]=t[2]+1
	print t

def logistic(ytrain,xtrain,ytest,xtest):
	Ytrain = np.array(ytrain)
	Xtrain = np.array(xtrain)
	Ytest = np.array(ytest)
	Xtest = np.array(xtest)
	#a = np.array(x)
	#b = np.array(y)
	lr = LogisticRegression().fit(Xtrain,Ytrain)
	yhat = lr.predict(Xtest)
	print lr.coef_
	print " "
	#print accuracy_score(ytest,yhat)
	return yhat

date = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i in range(0,len(date)):
	#print date[i]
	print " "
	data = []
	Files = ["logistic_new_flightfreq_data_"+date[i]]
	for File in Files:
		ifile  = open(File+'.csv', "rb")
		reader = csv.reader(ifile)
		for row in reader:
			data.append(row)
		ifile.close()

	random.shuffle(data)
	CrossValidation(data)
	print " "

print " "
data = []
Files = ["logistic_new_flightfreq_data"]
for File in Files:
	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)
	ifile.close()

random.shuffle(data)
CrossValidation(data)
print " "
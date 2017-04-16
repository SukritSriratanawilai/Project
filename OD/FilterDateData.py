import random
import sys
import csv
import nltk.tokenize
import math
from numpy import arange,array,ones,linalg
from pylab import plot,show

# Load the diabetes dataset

filter1 = ["Jan2013"]
filter2 = ["Jan2013","Feb2013","Mar2013","Apr2013","May2013","Jun2013"]
filter3 = ["Jan2013","Feb2013","Mar2013","Apr2013","May2013","Jun2013","Jul2013","Aug2013","Sep2013","Oct2013","Nov2013","Dec2013"]
filter4 = ["Jan2013","Feb2013","Mar2013","Apr2013","May2013","Jun2013","Jul2013","Aug2013","Sep2013","Oct2013","Nov2013","Dec2013","Jan2014","Feb2014","Mar2014","Apr2014","May2014","Jun2014"]
filter5 = ["Jan2013","Feb2013","Mar2013","Apr2013","May2013","Jun2013","Jul2013","Aug2013","Sep2013","Oct2013","Nov2013","Dec2013","Jan2014","Feb2014","Mar2014","Apr2014","May2014","Jun2014","Jul2014","Aug2014","Sep2014","Oct2014","Nov2014","Dec2014","Jan2015","Feb2015","Mar2015","Apr2015","May2015","Jun2015","Jul2015","Aug2015","Sep2015","Oct2015","Nov2015","Dec2015"]

data = []
Files = ['test_2013']
for File in Files:

	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		data.append(row)
	ifile.close()

output = []
#output.append(data[0])
for i in data:
	for x in filter5:
		if i[2] == x:
			output.append(i)

b = open('OD_3years.csv', 'w')
a = csv.writer(b,quoting=csv.QUOTE_ALL,lineterminator="\n")
a.writerows(output)
b.close()		

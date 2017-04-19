import random
import sys
import csv
import nltk.tokenize
import math
from numpy import arange,array,ones,linalg
from pylab import plot,show
import re

sumation = []
Files = ['sumation_3years']
for File in Files:

	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		sumation.append(row)
	ifile.close()

print sumation[1][0]

OD = []
Files = ['AlldataOD']
for File in Files:

	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		OD.append(row)
	ifile.close()

print OD[0][2]
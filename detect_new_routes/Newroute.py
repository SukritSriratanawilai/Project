import random
import sys
import csv
import nltk.tokenize
import math
from numpy import arange,array,ones,linalg
from pylab import plot,show
import re
# Load the diabetes dataset
def search_income(date,origin,destination,income):
	income_org = []
	for i in range(1,len(income)):
		if origin == income[i][0]:
			income_org = income[i]
				#print income[i]
	income_dest = []
	for i in range(1,len(income)):
		if destination == income[i][0]:
			income_dest = income[i]
	if re.search('2013',date):
		year_index = 5
	elif re.search('2014',date):
		year_index = 6
	elif re.search('2015',date):
		year_index = 7
	else:
		print "error"
	out = [float(income_org[year_index]),float(income_dest[year_index]),float(income_org[year_index+3]),float(income_dest[year_index+3])]
	#print out
	#print origin + " " + destination + " " + date
	#print " "
	return out

def join(OD,income,sumation,index):
	a = []
	a.append(["Op Airlines","Original","Destination","Passenger","Fare","Income Original","Income Destination","Population Original","Population Destination","Date","Flight Frequency","Total Seat","Seat/Dep","Time","AVG KM","Number Of Review","Airlines Score"])
	#print len(OD[0])
	#print len(sumation[0])
	for j in range(0,len(OD)):
		income_org = []
		for i in range(1,len(income)):
			if OD[j][1] == income[i][0]:
				income_org = income[i]
				#print income[i]
		income_dest = []
		for i in range(1,len(income)):
			if OD[j][2] == income[i][0]:
				income_dest = income[i]
				#print income[i]
		sum_temp = []
		for i in range(1,len(sumation)):
			if sumation[i][0] == OD[j][5] and sumation[i][1] == OD[j][0] and sumation[i][2] == OD[j][1] and sumation[i][3] == OD[j][2]:
				sum_temp = sumation[i]
				#print sum_temp
				#a.append(sum_temp)

		index_temp = []
		for i in range(1,len(index)):
			if OD[j][0] == index[i][4]:
				index_temp = index[i]
		year_index = 0
		if re.search('2013',OD[j][5]):
			year_index = 5
		elif re.search('2014',OD[j][5]):
			year_index = 6
		elif re.search('2015',OD[j][5]):
			year_index = 7
		else:
			print "error"

		if len(income_org) != 0 and len(income_dest) != 0 and len(sum_temp)!= 0:
		#select.append([temp[7],temp[15],temp[22],temp2[1],temp2[6],float(income_org[5]),float(income_dest[5])])
			a.append([OD[j][0],OD[j][1],OD[j][2],OD[j][3],OD[j][4],float(income_org[year_index]),float(income_dest[year_index]),float(income_org[year_index+3]),float(income_dest[year_index+3]),sum_temp[0],sum_temp[4],sum_temp[5],sum_temp[6],sum_temp[7],sum_temp[8],float(index_temp[1]),float(index_temp[2])])
		#	sum_temp = []
	return a

def find_data(input_data, income, index):
	#print input_data[0]
	#y2014 = []
	#y2015 = []
	yes = []
	no = []
	out = []
	#check = []
	for i in range(1,len(input_data)):
		#print input_data[i][9]
		temp = []
		for j in range(0,10):
			temp.append(input_data[i][j])
		temp.append(input_data[i][16])
		temp.append(1)
		yes.append(temp)
		if re.search('2014',input_data[i][9]):
		#	y2014.append(input_data[i])
			temp2 = []
			for j in range(0,3):
				temp2.append(input_data[i][j])
			temp2.append(0)
			temp2.append(0)
			date = input_data[i][9].replace('2014','2013')
			#print input_data[i][9]
			income_and_pop = search_income(date,temp2[1],temp2[2],income)
			for j in range(0,len(income_and_pop)):
				temp2.append(income_and_pop[j])
			temp2.append(date)
			temp2.append(input_data[i][16])
			temp2.append(0)
			no.append(temp2)
			
			#check.append([input_data[i][9],date])
		elif re.search('2015',input_data[i][9]):
			#print input_data[i][9]
		#	y2015.append(input_data[i])
			temp2 = []
			for j in range(0,3):
				temp2.append(input_data[i][j])
			temp2.append(0)
			temp2.append(0)
			date = input_data[i][9].replace('2015','2014')
			#print input_data[i][9]
			income_and_pop = search_income(date,temp2[1],temp2[2],income)
			for j in range(0,len(income_and_pop)):
				temp2.append(income_and_pop[j])
			temp2.append(date)
			temp2.append(input_data[i][16])
			temp2.append(0)
			no.append(temp2)

			temp2 = []
			for j in range(0,3):
				temp2.append(input_data[i][j])
			temp2.append(0)
			temp2.append(0)
			date = input_data[i][9].replace('2015','2013')
			#print date
			#print input_data[i][9]
			income_and_pop = search_income(date,temp2[1],temp2[2],income)
			for j in range(0,len(income_and_pop)):
				temp2.append(income_and_pop[j])
			temp2.append(date)			
			temp2.append(input_data[i][16])
			temp2.append(0)
			no.append(temp2)
	#print len(y2014)
	#print len(y2015)
	#print len(no)
	#print len(yes)
	
	random.shuffle(no)
	for i in range(0,len(yes)):
		out.append(yes[i])
	for i in range(0,len(yes)):
		out.append(no[i])
	for i in out:
		print i
	return out

income = []
Files = ['income_and_pop_v1']
for File in Files:

	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		income.append(row)
	ifile.close()

sumation = []
Files = ['sumation_3years']
for File in Files:

	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		sumation.append(row)
	ifile.close()

index = []
Files = ['ThaiAirIndex']
for File in Files:

	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		index.append(row)
	ifile.close()

OD = []
Files = ['AlldataOD']
for File in Files:

	ifile  = open(File+'.csv', "rb")
	reader = csv.reader(ifile)
	for row in reader:
		OD.append(row)
	ifile.close()

select = []
#select.append(["Op Airlines","Original","Destination","Passenger","Fare","Income Original","Income Destination","Population Original","Population Destination","Date","Flight Frequency","Total Seat","Seat/Dep","Time","AVG KM","Number Of Review","Airlines Score"])
for k in range(0,len(OD)):

	data = OD[k]
	date = data[2]

	data[0] = data[0].replace('[','')
	data[0] = data[0].replace(']','')
	data[0] = data[0].replace('\'','')
	temp = data[0].split(',')

	for i in range(0,len(temp)):
		temp[i] = temp[i].replace(' ','')

	data[1] = data[1].replace('[','')
	data[1] = data[1].replace(']','')
	data[1] = data[1].replace('\'','')

	temp2 = data[1].split()

	for i in range(0,len(temp2)):
		temp2[i] = float(temp2[i].replace(',' , ''))
	if  not(re.search('2016',date)):
		select.append([temp[7],temp[15],temp[22],temp2[1],temp2[6],date])
new_route = []
j = 0
while j < len(select):
	check = False
	if select[j][3] == 0:
		check = True
	if check:	
		for i in range(j,j+36):
			if select[i][3] > 2 :
				new_route.append(select[i])
				break
			#print select[i]
		#print type(select[i][3])
	j = j+36

for i in new_route:
	print i
print len(new_route)

output = join(new_route,income,sumation,index)
trainset_0 = find_data(output,income,index)
b = open('logistic_data.csv', 'w')
a = csv.writer(b,quoting=csv.QUOTE_ALL,lineterminator="\n")
a.writerows(trainset_0)
b.close()	
#b = open('new_route_data_ver1.csv', 'w')
#a = csv.writer(b,quoting=csv.QUOTE_ALL,lineterminator="\n")
#a.writerows(output)
#b.close()		

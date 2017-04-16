import numpy as np
import statsmodels.api as sm
from sklearn import preprocessing


y = [1,2,3,4,3,4,5,4,5,5,4,5,4,5,4,5,6,5,4,5,4,3,4]

x = [
     [4,2,3,4,5,4,5,6,7,4,8,9,8,8,6,6,5,5,5,5,5,5,5],
     [4,1,2,3,4,5,6,7,5,8,7,8,7,8,7,8,7,7,7,7,7,6,5],
     [4,1,2,5,6,7,8,9,7,8,7,8,7,7,7,7,7,7,6,6,4,4,4]
     ]

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

print len(x[0])
print len(y)
print reg_m(y, x).summary()

#xx = preprocessing.scale(x)

#print xx
#print xx.mean(axis=0)
#print xx.std(axis=0)
#xx = preprocessing.normalize(x)
#print xx
x = [[5,4,3,2,1],[1,2,3,4,5]]
x2 = [1,2,3,4,5]
xx = preprocessing.normalize(x)
print xx
#xx = preprocessing.scale(x2)
#print xx
#print xx.mean(axis=0)
#print xx.std(axis=0)

#a = 0
#for i in xx:
 #   a = a + i

#print a

x = [70.0,55.0,98.0,72.0,14.0,25.0,16.0]
print max(x)
print min(x)

print float(16-14)/float(98-14)
n = normalization(x)
print n
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# data from columns A - D
Xtrain = np.array([[1,    20,   30,   1],
                   [2,    22,   12,   33],
                   [3,    45,   65,   77],
                   [12,   43,   55,   65],
                   [11,   25,   30,   1],
                   [22,   23,   19,   31],
                   [31,   41,   11,   70],
                   [1,    48,   23,   60]])

# data from column E
ytrain = np.array([1, 2, 3, 4, 1, 2, 3, 4])



lr = LogisticRegression().fit(Xtrain, ytrain)

yhat = lr.predict(Xtrain)

print ytrain
print yhat

print accuracy_score(ytrain, yhat)

import random

foo = ['a', 'b', 'c', 'd', 'e']
random.shuffle(foo)
print foo

print type(Xtrain)
print type(ytrain)
z = []
for i in range(3):
	z.append(Xtrain[i])
for i in range(5,len(Xtrain)):
	z.append(Xtrain[i])

print z
b = np.array(z)
print b
import numpy as np
from numpy.linalg import inv
from scipy import stats as s
from scipy.stats import multivariate_normal as mn
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

H = np.loadtxt('/home/user/PRTakeHome1/train_sp2015_v14')
St= np.loadtxt('/home/user/PRTakeHome1/test_sp2015_v14')

#class 1 and 2
X = np.ones((15000, 1))
X = np.concatenate( (X, H), axis = 1) 
class1 = X[0:5000]
class2 = X[5000:10000]
class3 = X[10000:15000]

a12 = np.ones((5,1))
b12 = np.ones((10000, 1))
Y12 = np.concatenate((class1, -1*class2), axis = 0)
alpha = 0.1
check = Y12.dot(a12)
#count = 0
#print Y.dot(a).shape
prevb12 = np.zeros((10000, 1))
while( True ):
    #count = count + 1
    e = check-b12
    b12 = b12+alpha*(e + abs(e))
    if( (prevb12 == b12).all() ):
        break
    prevb12 = b12
    temp = inv(Y12.T.dot(Y12)).dot(Y12.T)
    a12 = temp.dot(b12)
    check = Y12.dot(a12)
#print check
#print count
# cl1 = 0
# cl2 = 0
# tempvar = 0
# for i in range(10000):
#     tempvar = Y12[i].dot(X[i].T)-b12[i]
#     if( tempvar > 0):
#         cl1 = cl1 + 1
#     else:
#         cl2 = cl2 + 1

# print cl1
# print cl2
print a12
print b12.shape

#class 2 and 3
X = np.ones((15000, 1))
X = np.concatenate( (X, H), axis = 1) 
class1 = X[0:5000]
class2 = X[5000:10000]
class3 = X[10000:15000]

a23 = np.ones((5,1))
b23 = np.ones((10000, 1))
Y23 = np.concatenate((class2, -1*class3), axis = 0)
alpha = 0.1
check = Y23.dot(a23)
#count = 0
#print Y.dot(a).shape
prevb23 = np.zeros((10000, 1))
while( True ):
    #count = count + 1
    e = check-b23
    b23 = b23+alpha*(e + abs(e))
    if( (prevb23 == b23).all() ):
        break
    prevb23 = b23
    temp = inv(Y23.T.dot(Y23)).dot(Y23.T)
    a23 = temp.dot(b23)
    check = Y23.dot(a23)
#print check
#print count
# cl2 = 0
# cl3 = 0
# tempvar = 0
# for i in range(10000):
#     tempvar = Y23[i].dot(X[i+5000].T)-b23[i]
#     if( tempvar > 0):
#         cl2 = cl2 + 1
#     else:
#         cl3 = cl3 + 1

# print cl2
# print cl3
print a23

#class 1 and 3
X = np.ones((15000, 1))
X = np.concatenate( (X, H), axis = 1) 
class1 = X[0:5000]
class2 = X[5000:10000]
class3 = X[10000:15000]

a13 = np.ones((5,1))
b13 = np.ones((10000, 1))
Y13 = np.concatenate((class1, -1*class3), axis = 0)
alpha = 0.1
check = Y13.dot(a13)
#count = 0
#print Y.dot(a).shape
prevb13 = np.zeros((10000, 1))
while( True ):
    #count = count + 1
    e = check-b13
    b13 = b13+alpha*(e + abs(e))
    if( (prevb13 == b13).all() ):
        break
    prevb13 = b13
    temp = inv(Y13.T.dot(Y13)).dot(Y13.T)
    a13 = temp.dot(b13)
    check = Y13.dot(a13)
#print check
#print count
# cl1 = 0
# cl3 = 0
# tempvar = 0
# for i in range(5000):
#     tempvar = Y13[i].dot(X[i].T)-b13[i]
#     if( tempvar > 0):
#         cl1 = cl1 + 1
#     else:
#         cl3 = cl3 + 1
# print cl1
# print cl3       
# for i in range(5000, 10000):
#     tempvar = Y13[i].dot(X[i+5000].T)-b13[i]
#     if( tempvar > 0):
#         cl1 = cl1 + 1
#     else:
#         cl3 = cl3 + 1

# print cl1
# print cl3
print a13



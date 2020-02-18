from sklearn.feature_extraction import text
from sklearn.decomposition import TruncatedSVD
from sklearn.svm import SVR
from  kappa  import quadratic_weighted_kappa

import pickle
import numpy as np
from sklearn.preprocessing import minmax_scale

x_train_path = "./ModelSystem/Features/X_train.pickle"

with open(x_train_path,"rb") as f:
    x_train = pickle.load(f)

y_train_path = "./ModelSystem/Features/Y_train.pickle"

with open(y_train_path,"rb") as f:
    y_train = pickle.load(f)


hist = np.bincount(y_train)
cdf = np.cumsum(hist) / float(sum(hist))

'''
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(\
    x_train,y_train,test_size = 0.3,random_state = 0)
'''
sz = 7000

x_test = x_train[sz:]
y_test = y_train[sz:]
x_train = x_train[:sz]
y_train = y_train[:sz]



#获取样本权重
def getWeights():
    import pandas as pd
    dfTrain =pd.read_csv('./ModelSystem/RawData/train.csv')
    var = list(dfTrain["relevance_variance"])
    weights = []
    for v in var:
        weights.append(1/(float(v) + 1.0))
    weights = np.array(weights,dtype=float)
    #print(weights)
    return weights[:sz]

def rounding_cdf(y_pred):
    y_pred = np.array(y_pred)
    sz =len(y_pred)
    y_index = y_pred.argsort()
    s = 0
    for i in range(4):
        t = cdf[i]*sz
        for j in range(int(s),int(t)):
            y_pred[ y_index[j] ] = i
        s = t

    y_pred = y_pred.astype(np.int32)
    return y_pred


def calcAcc(A,B):
    sz = len(A)
    acc=0

    m = np.zeros([4,4],dtype=int)
    for i in range(sz):
        if(A[i]==B[i]):acc+=1
        m[A[i]][B[i]]+=1
    
    print(m)

    return acc/sz


def svr():

    clf = SVR(C=4.0,gamma=0.2,cache_size=2048,kernel='rbf')
    clf.fit(x_train,y_train,sample_weight=getWeights())#,sample_weight=weights)
    y_pred = clf.predict(x_test)

    y_pred = list(y_pred)
    y_p = rounding_cdf(y_pred)

    qwk=quadratic_weighted_kappa(y_test,y_p)
    print("SVR Kappa:",qwk)


svr()
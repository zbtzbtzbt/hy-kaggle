from sklearn.model_selection import cross_val_score

from hyperopt import hp,STATUS_OK,Trials,fmin,tpe
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import cohen_kappa_score
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC

from sklearn.linear_model import Ridge
from kappa import quadratic_weighted_kappa

x_train_path = "./X_train.pickle"

with open(x_train_path,"rb") as f:
    x_train = pickle.load(f)

y_train_path = "./Y_train.pickle"

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
    print("Get Weight Success")
    return weights[:sz]


def hyperopt_train_test(params):

    #model chosen
    # clf = RandomForestClassifier(**params, n_jobs=8, max_features='auto', max_depth=None, criterion='gini')
    # clf = SVC(**params)
    # clf.fit(x_train,y_train,sample_weight=getWeights())
    # Y_predict=clf.predict(x_test)
    # clf=xgb(**params,n_jobs=8)
    # clf= LinearRegression(**params,n_jobs=-1)
    clf = Ridge(**params)
    return cross_val_score(clf, x_train, y_train).mean()
    # return quadratic_weighted_kappa(Y_predict,y_test)
best = 0
space = {
    #SVM para
    # 'C': hp.uniform('C', 0, 200),
    # 'kernel': hp.choice('kernel', ['linear', 'sigmoid', 'poly', 'rbf']),
    # 'gamma': hp.uniform('gamma', 0, 200),

    #RF para
    # 'n_estimators': hp.choice('n_estimators', range(100,500)),
    # 'min_samples_leaf':hp.choice('min_samples_leaf',range(1,10)),
    # 'min_samples_split':hp.uniform('min_samples_split',0,0.99),

    # XGBoost para
    # 'learning_rate':hp.uniform('learning_rate',0.01,0.2),
    # 'max_depth':hp.choice('max_depth',range(3,10)),
    # 'n_estimator':hp.choice('n_estimator',range(100,1000)),

    # LR para

    # Ridge para
    'alpha':hp.uniform('alpha',0.001,0.999),
    'max_iter':hp.choice('max_iter',500,5000),
    'solver':hp.choice('solver',['auto','svd','cholesky','lsqr','sparse_cg','sag'])
}


def f(params):
    global best
    acc = hyperopt_train_test(params)
    if acc > best:
        best = acc
    print('new best:', best, params)
    return {'loss': -acc, 'status': STATUS_OK}


trials = Trials()
# chosen max_evals
best = fmin(f, space, algo=tpe.suggest, max_evals=300, trials=trials)

# import os
#save best
doc=open('SVR_best.txt','a+')
print('best:', best)
print('best:', best,file=doc)
doc.close()
###################################


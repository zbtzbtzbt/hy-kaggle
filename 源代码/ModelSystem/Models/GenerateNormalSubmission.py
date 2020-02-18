from sklearn.feature_extraction import text
from sklearn.decomposition import TruncatedSVD
from sklearn.svm import SVR
from  kappa  import quadratic_weighted_kappa

import pickle
import numpy as np
from sklearn.preprocessing import minmax_scale
import pandas as pd

x_train_path = "./ModelSystem/Features/X_train.pickle"

with open(x_train_path,"rb") as f:
    x_train = pickle.load(f)

y_train_path = "./ModelSystem/Features/Y_train.pickle"

with open(y_train_path,"rb") as f:
    y_train = pickle.load(f)


x_test_path = "./ModelSystem/Features/X_test.pickle"
with open(x_test_path,"rb") as f:
    x_test = pickle.load(f)

hist = np.bincount(y_train)
cdf = np.cumsum(hist) / float(sum(hist))
print("cdf =",cdf)

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
    return weights

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

    cnt = np.zeros([4])
    for i in y_pred:
        cnt[i] += 1

    print("rounding cdf cnt=",cnt)
    return y_pred



def svr(sample_weight):

    clf = SVR(C=4.0,gamma=0.2,cache_size=2048,kernel='rbf')
    clf.fit(x_train,y_train,sample_weight=sample_weight)#,sample_weight=weights)
    y_pred = clf.predict(x_test)

    y_pred = list(y_pred)
    y_pred = rounding_cdf(y_pred)
    return y_pred



def lir(sample_weight):
    from sklearn.linear_model import LinearRegression
    
    model = LinearRegression(n_jobs = -1)
    model.fit(x_train, y_train,sample_weight=sample_weight)
    y_pred = model.predict(x_test)
    y_pred = list(y_pred)

    y_p = rounding_cdf(y_pred)
    return y_p

    #submission = pd.read_csv("./ModelSystem/RawData/sampleSubmission.csv")
  
    #print(len(y_pred))
    #print(len(submission["prediction"]))

    #for i in range(len(y_pred)):
    #    y_pred[i] = y_pred[i] +1
        #submission["prediction"][i] =  y_pred[i]
    
    #submission.to_csv("./ModelSystem/Models/NormalSubmission.csv",index=False)

def ridge(sample_weight, alpha=1.0):
    from sklearn.linear_model import Ridge
    ridge = Ridge(alpha=alpha, normalize=False)
    ridge.fit(x_train, y_train,sample_weight=sample_weight)#, sample_weight=weight_train[index_base]
    y_pred = ridge.predict(x_test)

    y_pred = list(y_pred)
    y_p = rounding_cdf(y_pred)
    return y_p


import numpy as np
def softmax(x):
    exp_x = np.exp(x)
    softmax_x = exp_x / np.sum(exp_x)
    return softmax_x

if __name__ == "__main__":

    #获取样本权重
    sample_weight = getWeights()
    svr_pred = svr(sample_weight)    
    linear_pred = lir(sample_weight)
    ridge_pred = ridge(sample_weight)

    submission = pd.read_csv("./ModelSystem/RawData/sampleSubmission.csv")
    print("Sample Count = ",len(svr_pred))

    #生成svr的结果
    for i in range(len(svr_pred)):
        submission["prediction"][i] =  svr_pred[i] + 1
    
    submission.to_csv("./ModelSystem/Models/NormalSubmission_svr.csv",index=False)

    #lr
    for i in range(len(linear_pred)):
        submission["prediction"][i] =  linear_pred[i] + 1
    
    submission.to_csv("./ModelSystem/Models/NormalSubmission_lir.csv",index=False)

    #ridge
    for i in range(len(ridge_pred)):
        submission["prediction"][i] =  ridge_pred[i] + 1
    
    submission.to_csv("./ModelSystem/Models/NormalSubmission_ridge.csv",index=False)

    x = [0.68964, 0.65192, 0.64851]
    x = softmax(x)
    
    svr_pred = svr_pred.astype(np.float)
    linear_pred = linear_pred.astype(np.float)
    ridge_pred = ridge_pred.astype(np.float)

    final_relevance =x[0]*svr_pred+x[1]*linear_pred+x[2]*ridge_pred
    final_relevance_cp = final_relevance.copy()
    final_relevance = rounding_cdf(final_relevance)

    #生成提交文件


    for i in range(len(final_relevance)):
        submission["prediction"][i] =  final_relevance[i]+1
    
    submission.to_csv("./ModelSystem/Models/NormalSubmission_final.csv",index=False)

    #生成结果文件供search system使用
    svr_pred = svr_pred.astype(np.int32)
    linear_pred = linear_pred.astype(np.int32)
    ridge_pred = ridge_pred.astype(np.int32)

    save = open('./SearchSystem/data/result.pickle', 'wb')
    data=[svr_pred,linear_pred,ridge_pred,final_relevance_cp]
    pickle.dump(data, save)
    save.close()
#import cfg
import pandas as pd
import numpy as np
import scipy.sparse as sp
import re
import  pickle

with open("./ModelSystem/Features/group5/" + 'train_df.pickle',"rb") as f:
    train_df = pickle.load(f)

with open("./ModelSystem/Features/group5/" + 'test_df.pickle',"rb") as f:
    test_df = pickle.load(f)


tsne_title_1_train = list(train_df['tsne_title_1'])
tsne_title_2_train = list(train_df['tsne_title_2'])
tsne_title_1_test = list(test_df['tsne_title_1'])
tsne_title_2_test = list(test_df['tsne_title_2'])

tsne_qt_1_train = list(train_df['tsne_qt_1'])
tsne_qt_2_train = list(train_df['tsne_qt_2'])
tsne_qt_1_test = list(test_df['tsne_qt_1'])
tsne_qt_2_test = list(test_df['tsne_qt_2'])

tsne_desc_1_train = list(train_df['tsne_desc_1'])
tsne_desc_2_train = list(train_df['tsne_desc_2'])
tsne_desc_1_test = list(test_df['tsne_desc_1'])
tsne_desc_2_test = list(test_df['tsne_desc_2'])


trainFeatures = np.array( [tsne_title_1_train,tsne_title_2_train,\
    tsne_qt_1_train,tsne_qt_2_train,\
    tsne_desc_1_train, tsne_desc_2_train] ,dtype=float  )

trainFeatures=trainFeatures.transpose()

testFeatures = np.array( [tsne_title_1_test,tsne_title_2_test,\
    tsne_qt_1_test,tsne_qt_2_test,\
    tsne_desc_1_test, tsne_desc_2_test] ,dtype=float  )

testFeatures=testFeatures.transpose()

print("trainFeatures.shape=" ,trainFeatures.shape)
print("testFeatures.shape=" ,testFeatures.shape)

with open("./ModelSystem/Features/group5/" + 'group5_train.pickle',"wb") as f:
    pickle.dump(trainFeatures, f)

with open("./ModelSystem/Features/group5/" + 'group5_test.pickle',"wb") as f:
    pickle.dump(testFeatures,f)


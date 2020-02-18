
import pandas as pd
dfTrain =pd.read_csv('./ModelSystem/ProcessedData/train.csv')
dfTest = pd.read_csv('./ModelSystem/ProcessedData/test.csv')

names = ["query", "title", "description"]
columns = ['query','product_title','product_description']


import pickle
for i in range(3):
    data = list(dfTrain[columns[i]])

    with open("./ModelSystem/ProcessedData/%s_train.pickle" % names[i],"wb") as f:
        pickle.dump(data,f)
    print (len(data))

for i in range(3):
    data = list(dfTest[columns[i]])

    with open("./ModelSystem/ProcessedData/%s_test.pickle" % names[i],"wb") as f:
        pickle.dump(data,f)




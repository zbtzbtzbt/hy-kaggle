
import pandas as pd
import pickle
import numpy as np
import scipy.sparse as sp

'''
先使用
GenerateTFIDFSparseMatrix.py

'''


def generateTFIDFFeatures():

    #读入tfidf矩阵
    file = open("./ModelSystem/Features/tfidf/"+ "tfidfSparseMatrix.pickle","rb")
    tfidfSparseMatrix = pickle.load(file)
    file.close()
    features =  tfidfSparseMatrix.shape[1]

    file = open("./ModelSystem/ProcessedData/"+ "query_train.pickle","rb")
    query_train=pickle.load(file)
    file.close()
    trainSz = len(query_train)
    del query_train

    
    nonzeroPos  = tfidfSparseMatrix.nonzero()
    nonzeroPosX = nonzeroPos[0]
    nonzeroPosY = nonzeroPos[1]
        
    print("trainSz = ",trainSz)
    ##############
    #train set
    ##############
    
    ############
    #tfidfQuery-train
    ############
    #tfidfQuery = np.zeros([trainSz,features],dtype = float)
    tfidfQuery = sp.lil_matrix((trainSz, features),dtype = float)
    #((3, 4), dtype=np.int8).toarray()
    for i in range(len(nonzeroPosX)):
        x = nonzeroPosX[i]
        y = nonzeroPosY[i]
        if(x % 3!=0):
            continue
        if( x//3 >= trainSz):
            break
        #tfidfQuery[x//3][y] = tfidfSparseMatrix[x,y]
        tfidfQuery[x//3,y] = tfidfSparseMatrix[x,y]

    
    file = open("./ModelSystem/Features/tfidf/"+ "tfidf_query_train.pickle","wb")
    pickle.dump(sp.csr_matrix(tfidfQuery),file)
    file.close()
    del tfidfQuery
    
    ############
    #tfidfProductTitle-train
    ############
    #tfidfProductTitle = np.zeros([trainSz,features],dtype = float)
    tfidfProductTitle = sp.lil_matrix((trainSz, features),dtype = float)
    
    for i in range(len(nonzeroPosX)):
        x = nonzeroPosX[i]
        y = nonzeroPosY[i]
        if((x-1) % 3!=0):
            continue
        if( (x-1)//3 >= trainSz):
            break
        #tfidfProductTitle[(x-1)//3][y] = tfidfSparseMatrix[x,y]
        tfidfProductTitle[(x-1)//3,y] = tfidfSparseMatrix[x,y]

    file = open("./ModelSystem/Features/tfidf/"+ "tfidf_title_train.pickle","wb")
    pickle.dump(sp.csr_matrix(tfidfProductTitle),file)
    file.close()
    del tfidfProductTitle

    ############
    #tfidfProductDescription-train
    ############
    #tfidfProductDescription = np.zeros([trainSz,features],dtype = float)
    tfidfProductDescription = sp.lil_matrix((trainSz, features),dtype = float)
    for i in range(len(nonzeroPosX)):
        x = nonzeroPosX[i]
        y = nonzeroPosY[i]
        if((x-2) % 3!=0):
            continue
        if( (x-2)//3 >= trainSz):
            break
        #tfidfProductDescription[(x-2)//3][y] = tfidfSparseMatrix[x,y]
        tfidfProductDescription[(x-2)//3,y] = tfidfSparseMatrix[x,y]

    file = open("./ModelSystem/Features/tfidf/"+ "tfidf_description_train.pickle","wb")
    pickle.dump(sp.csr_matrix(tfidfProductDescription),file)
    file.close()
    del tfidfProductDescription

    
    ##############
    #test set
    ##############
    file = open("./ModelSystem/ProcessedData/"+ "query_test.pickle","rb")
    query_test=pickle.load(file)
    file.close()
    testSz = len(query_test)
    del query_test

    

    nonzeroPos  = tfidfSparseMatrix.nonzero()
    nonzeroPosX = nonzeroPos[0]
    nonzeroPosY = nonzeroPos[1]
        
    print("testSz = ",testSz)
    #print(tfidfSparseMatrix.shape)
    #return

    ############
    #tfidfQuery-test
    ############
    #tfidfQuery = np.zeros([testSz,features],dtype = float)
    tfidfQuery = sp.lil_matrix((testSz, features),dtype = float)
    for i in range(len(nonzeroPosX)):
        x = nonzeroPosX[i]
        y = nonzeroPosY[i]

        if(x<trainSz*3):
            continue

        if( (x-trainSz*3) % 3!=0):
            continue
        #tfidfQuery[(x-trainSz*3)//3][y] = tfidfSparseMatrix[x,y]
        tfidfQuery[(x-trainSz*3)//3,y] = tfidfSparseMatrix[x,y]
    
    file = open("./ModelSystem/Features/tfidf/"+ "tfidf_query_test.pickle","wb")
    pickle.dump(sp.csr_matrix(tfidfQuery),file)
    file.close()
    del tfidfQuery
    
    ############
    #tfidfProductTitle-test
    ############
    #tfidfProductTitle = np.zeros([testSz,features],dtype = float)
    tfidfProductTitle = sp.lil_matrix((testSz, features),dtype = float)
    for i in range(len(nonzeroPosX)):
        x = nonzeroPosX[i]
        y = nonzeroPosY[i]
        if(x<trainSz*3):
            continue

        if((x-1-trainSz*3) % 3!=0):
            continue
        
        #tfidfProductTitle[(x-1-trainSz*3)//3][y] = tfidfSparseMatrix[x,y]
        tfidfProductTitle[(x-1-trainSz*3)//3,y] = tfidfSparseMatrix[x,y]

    file = open("./ModelSystem/Features/tfidf/"+ "tfidf_title_test.pickle","wb")
    pickle.dump(sp.csr_matrix(tfidfProductTitle),file)
    file.close()
    del tfidfProductTitle

    ############
    #tfidfProductDescription-test
    ############
    #tfidfProductDescription = np.zeros([testSz,features],dtype = float)
    tfidfProductDescription = sp.lil_matrix((testSz, features),dtype = float)
    for i in range(len(nonzeroPosX)):
        x = nonzeroPosX[i]
        y = nonzeroPosY[i]
        if(x<trainSz*3):
            continue

        if((x-2-trainSz*3) % 3!=0):
            continue
        
        #tfidfProductDescription[(x-2-trainSz*3)//3][y] = tfidfSparseMatrix[x,y]
        tfidfProductDescription[(x-2-trainSz*3)//3,y] = tfidfSparseMatrix[x,y]

    file = open("./ModelSystem/Features/tfidf/"+ "tfidf_description_test.pickle","wb")
    pickle.dump(sp.csr_matrix(tfidfProductDescription),file)
    file.close()
    del tfidfProductDescription
    

def cos_sim(a,b):#a,b是两个csr_matrix
    sz  = a.shape[0]
    ret = np.zeros(shape=[sz,1])
    #print(sz)

    for i in range(sz):
        r1 = (a.getrow(i).todense())[0]
        r2 = (b.getrow(i).todense())[0]

        dotMul = r1.dot(r2.transpose())
        norm_1 = np.linalg.norm(r1)
        norm_2 = np.linalg.norm(r2)

        if(norm_1 == 0.0 or norm_2==0.0):
            pass
        else:
            ret[i][0] = dotMul / (norm_1 * norm_2)
    return sp.csr_matrix(ret)



def generateCosFeatures():

    ####################
    #CosSimilarity
    ####################
    #columnNames = ["query","title","description"]
    catagories = ["train","test"]
    for cata in catagories:
        with open("./ModelSystem/Features/tfidf/"+ "tfidf_query_%s.pickle" %(cata) ,"rb") as file:
            tfidf_query = pickle.load(file)

        with open("./ModelSystem/Features/tfidf/"+ "tfidf_title_%s.pickle" % (cata),"rb") as file:
            tfidf_title = pickle.load(file)

        with open("./ModelSystem/Features/tfidf/"+ "tfidf_description_%s.pickle" % cata,"rb") as file:
            tfidf_description = pickle.load(file)

        from sklearn.metrics.pairwise import cosine_similarity#, pairwise_distances

        tfidf_cos_query_title = cos_sim(tfidf_query, tfidf_title)
        tfidf_cos_query_description = cos_sim(tfidf_query, tfidf_description)
        tfidf_cos_title_description = cos_sim(tfidf_title, tfidf_description)

        print(len(tfidf_cos_query_title.nonzero()[0]))
        print(len(tfidf_cos_query_description.nonzero()[0]))
        print(len(tfidf_cos_title_description.nonzero()[0]))
        #tfidf_cos_query_title=sp.csr_matrix(tfidf_cos_query_title)

        with open("./ModelSystem/Features/tfidf/"+ "tfidf_cos_query_title_%s.pickle" % cata,"wb") as file:
            pickle.dump(tfidf_cos_query_title,file)

        with open("./ModelSystem/Features/tfidf/"+ "tfidf_cos_query_description_%s.pickle" % cata,"wb") as file:
            pickle.dump(tfidf_cos_query_description,file)

        with open("./ModelSystem/Features/tfidf/"+ "tfidf_cos_title_description_%s.pickle" % cata ,"wb") as file:
            pickle.dump(tfidf_cos_title_description,file)




def generateTFIDF_svd():
    from sklearn.decomposition import TruncatedSVD
    svd_n_components=100

    svd = TruncatedSVD(n_components=svd_n_components, n_iter=15)

    combineFeatures = [
        ("tfidf","tfidf_query"),
        ("tfidf","tfidf_title"),
        ("tfidf","tfidf_description"),
    ]

    featuresBasePath = "./ModelSystem/Features"
    #遍历combineFeatures中所有元素，依次找到特征对应的文件进行处理
    catagories = ["train","test"]
    trainSz =0
    testSz =0

    for i in range(len(combineFeatures)):
        print("Concatenate %d-th feature..." % i)
        wholeFeatureMatrix = None

        for cata in catagories:  
            featureCatagory,featureName = combineFeatures[i]
            path = "%s/%s/%s_%s.pickle" % (featuresBasePath,featureCatagory,featureName,cata)
            with open( path,"rb") as file:
                featureMatrix = pickle.load(file)
                #全部转换为csr矩阵
            if(type(featureMatrix) != sp.csr.csr_matrix):
                featureMatrix = sp.csr.csr_matrix(featureMatrix)

            if(cata == "train"):
                wholeFeatureMatrix = featureMatrix
                trainSz = featureMatrix.shape[0]
            else:
                testSz = featureMatrix.shape[0]
                wholeFeatureMatrix = sp.vstack((wholeFeatureMatrix,featureMatrix))
                print("whole matrix shape = ",wholeFeatureMatrix.shape)

        wholeFeatureMatrix  =  svd.fit_transform(wholeFeatureMatrix)
        print("SVDed whole matrix shape = ",wholeFeatureMatrix.shape)

        newPath = "%s/%s/%s_svd_train.pickle" % (featuresBasePath,featureCatagory,featureName)
        with open( newPath,"wb") as newFile:
            pickle.dump(wholeFeatureMatrix[:trainSz],newFile)

        newPath = "%s/%s/%s_svd_test.pickle" % (featuresBasePath,featureCatagory,featureName)
        with open( newPath,"wb") as newFile:
            pickle.dump(wholeFeatureMatrix[trainSz:],newFile)


def main():
    generateTFIDFFeatures()
    print(1)
    generateCosFeatures()
    print(2)

    generateTFIDF_svd()
    pass


if __name__ == "__main__":
    main()
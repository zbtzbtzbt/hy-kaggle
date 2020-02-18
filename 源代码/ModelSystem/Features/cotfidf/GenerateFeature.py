
import scipy.sparse as sp

import pickle
import joblib

def cooccurrence_terms(lst1, lst2, join_str):
    terms = [""] * len(lst1) * len(lst2)
    cnt =  0
    for item1 in lst1:
        for item2 in lst2:
            terms[cnt] = item1 + join_str + item2
            cnt += 1
    res = " ".join(terms)
    return res


features = ["query","title","description"]
ngrams = ["unigram","bigram"]
catagories = ["train","test"]

def generateRawCorpus():
    inputFolder = "./ModelSystem/Features/ngram"
    corpus = []


    with open( "%s/query_unigram_train.pickle" % inputFolder , "rb") as f:
        tmp = pickle.load(f)
        trainSz = len (tmp)
        print("trainSz=",trainSz)

    with open( "%s/query_unigram_test.pickle" % inputFolder , "rb") as f:
        tmp = pickle.load(f)
        testSz = len (tmp)
        print("testSz=",testSz)

    for i in range(len(features)):
        corpus.append([]) #[[]]
        for j in  range(len(ngrams)):  
            corpus[i].append([])#[[[]]]
            for k in range(len(catagories)):
                corpus[i][j].append([1])#[[[ 【】 ]]]
                with open( "%s/%s_%s_%s.pickle" % (inputFolder,features[i],ngrams[j],catagories[k]) , "rb") as f:
                    data = pickle.load(f)
                
                corpus[i][j][k] = data
                
                
                #print(data[0])

    return trainSz,testSz,corpus

def generateCorpusMatrix(trainSz,testSz,rawCorpus):

    corpus = []
    outputFolderPath="./ModelSystem/Features/cotfidf"
    
    for i in range(len(features)):
        corpus.append([]) #[[]]
        i1 = (i +1) % len(features)
        if(features[i]=="title" and features[i1]=="description"):continue
        
        #遍历ngram两两组合
        for j in  range(len(ngrams)):  
            corpus[i].append([]) #[[[]]]
            for j1 in range(len(ngrams)):
                corpus[i][j].append([]) #[[[[]]]]

                for k in range(len(catagories)):
                    corpus[i][j][j1].append([1]) #[[[[[]]]]]
                    print("[%d,%d,%d,%d] for [2,2,2,2]" % (i,j,j1,k))
                    #########l遍历所有样本，特征ngram两两组合
                    res = []
                    for l in range(len(rawCorpus[i][j][k])):
                        res.append( cooccurrence_terms(rawCorpus[i][j][k][l],rawCorpus[i1][j1][k][l],"_") )

                    corpus[i][j][j1][k] = res
                    '''
                    with open("%s/corpus_%s_%s_%s_%s_%s.pickle" % (outputFolderPath,features[i],ngrams[j],\
                        features[i1],ngrams[j1],catagories[k]) ,"wb") as f:
                        pickle.dump(res,f) 
                    '''
    #feature,ngram,ngram,cata,sample
    print(corpus[0][0][0][0][0])
    print(corpus[0][1][0][0][0])
    print(corpus[0][0][1][0][0])

    with open("%s/corpus_matrix.pickle" % (outputFolderPath) ,"wb") as f:
        pickle.dump(corpus,f) 

    '''
    #For Test
    for i in range(1):
        i1 = (i +1) % len(features)

        #遍历ngram两两组合
        for j in  range(1,2):  
            for j1 in range(1,2):
                for k in range(1):
                    #########l遍历所有样本，特征ngram两两组合
                    for l in range(5,6):
                        res = cooccurrence_terms(rawCorpus[i][j][k][l],rawCorpus[i1][j1][k][l],"_")
                        
                        print(res)
                        print("==========================")
    '''
 
def generateCoTFIDFSparseMatrix(trainSz,testSz):
    folderPath="./ModelSystem/Features/cotfidf"

    with open("%s/corpus_matrix.pickle" % (folderPath) ,"rb") as f:
        corpusMatrix = pickle.load(f) 
    
    #print(type(corpusMatrix[0][0][0][1]))
    #return 
    corpus = []

    cnt = 0

    pos= []

    for i in range(len(features)):
        i1 = (i +1) % len(features)
        if(features[i]=="title" and features[i1]=="description"):continue

        #遍历ngram两两组合
        for j in  range(len(ngrams)):  
            for j1 in range(len(ngrams)):
                for k in range(len(catagories)):
                    #########l遍历所有样本，特征ngram两两组合
                    #feature,ngram,ngram,cata,sample
                    s = len(corpus)
                    cnt += len(corpusMatrix[i][j][j1][k])
                    for l in range(len(corpusMatrix[i][j][j1][k])):
                        #corpusMatrix[i][j][j1][k][l] 一个string
                        #print(type(corpusMatrix[i][j][j1][k][l]))
                        corpus.append( corpusMatrix[i][j][j1][k][l])
                    t = len(corpus)
                    pos.append((s,t))
                    

    print("下面两行输出应该等于261368")
    print(cnt)
    print(len(corpus))

    with open("%s/corPos.pickle" % (folderPath),"wb") as f:
        pickle.dump(pos,f)

    print("开始生成coTF-IDF")
    from sklearn.feature_extraction.text import TfidfVectorizer

    vectorizer = TfidfVectorizer(min_df=3, # 最小支持度为2
        max_df=0.75,
        strip_accents='unicode',
        analyzer='word',
        token_pattern=r"(?u)\b\w\w+\b",
        ngram_range=(1, 1),  # 一元文法即可
        use_idf=1,
        smooth_idf=1,
        sublinear_tf=1,
        stop_words = 'english'
        #stop_words = None
        ) 

    tfidf = vectorizer.fit_transform(corpus)
    print(tfidf.shape)
    file = open("%s/cotfidfSparseMatrix.pickle" % (folderPath),"wb")
    pickle.dump(tfidf,file)
    file.close()
    print("coTF-IDF已生成")


def generateCoTFIDF(trainSz,testSz):
    folderPath="./ModelSystem/Features/cotfidf"
    #读入tfidf矩阵
    with open("%s/cotfidfSparseMatrix.pickle" % (folderPath) ,"rb") as f:
        tfidfSparseMatrix = pickle.load(f)

    with open("%s/corPos.pickle" % (folderPath),"rb") as f:
        corPos = pickle.load(f)

    print("tfidfSparseMatrix.shape = ",tfidfSparseMatrix.shape)
    
    indexInCorPos = 0
    rowCnt = 0
    for i in range(len(features)):
        i1 = (i +1) % len(features)
        if(features[i]=="title" and features[i1]=="description"):continue
        #遍历ngram两两组合
        for j in  range(len(ngrams)):  
            for j1 in range(len(ngrams)):
                for k in range(len(catagories)):

                    #feature,ngram,ngram,cata,sample
                    #coTFIDF是一个 2个特征2个ngram的coTFIDF矩阵
                    s,t = corPos[indexInCorPos]
                    print("From row ",s," To ",t)
                    indexInCorPos += 1
                    #coTFIDF = sp.csr_matrix((t-s, features),dtype = float)
                    #对应的是 tfidfSparseMatrix [s,t-1]

                    coTFIDF = tfidfSparseMatrix.getrow(s)

                    for l in range(s+1,t):
                        row = tfidfSparseMatrix.getrow(l)
                        coTFIDF = sp.vstack((coTFIDF,row))

                    print("coTFIDF.shape = ",coTFIDF.shape)
                    rowCnt += coTFIDF.shape[0]
                    coTFIDF = sp.csr_matrix(coTFIDF)
                    

                    with open("%s/cotfidf_%s_%s_%s_%s_%s.pickle" % (folderPath,features[i],ngrams[j],\
                        features[i1],ngrams[j1],catagories[k]) ,"wb") as f:
                        pickle.dump(coTFIDF,f) 
                    
                    print("总进度 ",rowCnt,"/",tfidfSparseMatrix.shape[0])
                    print("")

    print("%d = %d",rowCnt,tfidfSparseMatrix.shape[0])               

def printFeaturesName():
    for i in range(len(features)):
        i1 = (i +1) % len(features)
        if(features[i]=="title" and features[i1]=="description"):continue
        #遍历ngram两两组合
        for j in  range(len(ngrams)):  
            for j1 in range(len(ngrams)):
                #("tfidf","tfidf_cos_query_title"),
                print("(\"cotfidf\",\"cotfidf_%s_%s_%s_%s\")," % (features[i],ngrams[j],\
                    features[i1],ngrams[j1]))

         
if  __name__ == "__main__":
    print("Start")
    #trainSz,testSz,rawCorpus = generateRawCorpus()
    #generateCorpusMatrix(trainSz,testSz,rawCorpus)
    #generateCoTFIDFSparseMatrix(trainSz,testSz)
    #generateCoTFIDF(trainSz,testSz)

    printFeaturesName()

    print("All Done")
    pass


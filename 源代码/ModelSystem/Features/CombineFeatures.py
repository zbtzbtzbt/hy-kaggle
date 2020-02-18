

import pandas as pd
import pickle
import numpy as np
import scipy.sparse as sp
from sklearn.preprocessing import minmax_scale
featuresBasePath = "./ModelSystem/Features"
#columnNames = ["query","title","description"]
#featureCatagories = ["tfidf"]

'''
with open("./ModelSystem/Features/X_train_new_group_svr.pickle","rb") as f:
    tmp = pickle.load(f)
    print(tmp.shape)
exit()
'''
combineFeatures = [
        #tfidf
        #("tfidf","tfidf_query"),
        #("tfidf","tfidf_title"),
        #("tfidf","tfidf_description"),
        ("tfidf","tfidf_query_svd"),
        ("tfidf","tfidf_title_svd"),
        ("tfidf","tfidf_description_svd"),
        ("tfidf","tfidf_cos_query_title"),
        ("tfidf","tfidf_cos_query_description"),
        ("tfidf","tfidf_cos_title_description"),

        #Cooccurrence TF-IDF Features
        
        #("cotfidf","cotfidf_query_unigram_title_unigram"),
        #("cotfidf","cotfidf_query_unigram_title_bigram"),
        #("cotfidf","cotfidf_query_bigram_title_unigram"),
        #("cotfidf","cotfidf_query_bigram_title_bigram"),
        #("cotfidf","cotfidf_description_unigram_query_unigram"),
        #("cotfidf","cotfidf_description_unigram_query_bigram"),
        #("cotfidf","cotfidf_description_bigram_query_unigram"),
        #("cotfidf","cotfidf_description_bigram_query_bigram"),
        
        #distance dice
        ("distance","dice_unigram_description_query"),
        ("distance","dice_unigram_query_title"),
        ("distance","dice_unigram_title_description"),

        ("distance","dice_bigram_description_query"),
        ("distance","dice_bigram_query_title"),
        ("distance","dice_bigram_title_description"),

        ("distance","dice_trigram_description_query"),
        ("distance","dice_trigram_query_title"),
        ("distance","dice_trigram_title_description"),

        #distance jaccard
        ("distance","jaccard_unigram_description_query"),
        ("distance","jaccard_unigram_query_title"),
        ("distance","jaccard_unigram_title_description"),

        ("distance","jaccard_bigram_description_query"),
        ("distance","jaccard_bigram_query_title"),
        ("distance","jaccard_bigram_title_description"),

        ("distance","jaccard_trigram_description_query"),
        ("distance","jaccard_trigram_query_title"),
        ("distance","jaccard_trigram_title_description"),

        #下面共48个
        #group1 #9
        ("group1","ratio_word_query_in_title"),
        ("group1","count_word_query_in_title"),
        ("group1","last_word_from_query_present_title"),
        ("group1","number_of_words_in_query"),
        ("group1","number_of_words_in_title"),
        ("group1","missing_indicator"),

        ("group1","compression_distance"),
        ("group1","edit_distance"),
        ("group1","mean_maximum_edit_distance"),
    

        #group2  6个
        ("group2","X5"),

        #group4 27个
        ("group4","group4"),

        #group5 6个
        ("group5","group5"),


    ]


def combineAllFeatures():


    catagories = ["train","test"]

    isToDense = False
    isToDense = True

    for cata in catagories:

        #if(cata=="test"):continue

        X = None
        #遍历combineFeatures中所有元素，依次找到特征对应的文件进行拼接
        for i in range(len(combineFeatures)):
            featureCatagory,featureName = combineFeatures[i]

            print("Concatenating %d-th %s feature : %s_%s" % (i,cata,featureName,cata))

            path = "%s/%s/%s_%s.pickle" % (featuresBasePath,featureCatagory,featureName,cata)
            with open( path,"rb") as file:
                featureMatrix = pickle.load(file)
                #全部转换为csr矩阵再拼接
                if(type(featureMatrix) != sp.csr.csr_matrix):
                    featureMatrix = sp.csr.csr_matrix(featureMatrix)

                if(i==0):
                    X = featureMatrix
                else:
                    X = sp.hstack((X,featureMatrix))           
                    #X = np.hstack((X,featureMatrix))
        
        if(isToDense):
            X = X.toarray()

        print(len(X.nonzero()[0]))
        print("X.shape = ",X.shape)

        if(isToDense):
            X = minmax_scale(X, axis=0)#归一化

        with open( "./ModelSystem/Features/X_%s.pickle" % cata,"wb") as file:
            pickle.dump(X,file)

        print("combineFeatures_%s Completed" % cata)
    print("All Done")

def main():
    combineAllFeatures()
    pass

if __name__ == "__main__":
    main()
    pass


import pandas as pd
import pickle
import numpy as np
import scipy.sparse as sp



"""
__file__

    genFeat_distance_feat.py

__description__

    This file generates the following features for each run and fold, and for the entire training and testing set.

        1. jaccard coefficient/dice distance between query & title, query & description, title & description pairs
            - just plain jaccard coefficient/dice distance
            - compute for unigram/bigram/trigram

        2. jaccard coefficient/dice distance stats features for title/description
            - computation is carried out with regard to a pool of samples grouped by:
                - median_relevance (#4)
                - query (qid) & median_relevance (#4)
            - jaccard coefficient/dice distance for the following pairs are computed for each sample
                - sample title        vs.  pooled sample titles
                - sample description  vs.  pooled sample descriptions
                Note that in the pool samples, we exclude the current sample being considered.
            - stats features include quantiles of cosine similarity and others defined in the variable "stats_func", e.g.,
                - mean value
                - standard deviation (std)
                - more can be added, e.g., moment features etc


"""


#####################
## Distance metric ##
#####################

def try_divide(x, y, val=0.0):
    """ 
    	Try to divide two numbers
    """
    if y != 0.0:
    	val = float(x) / y
    return val

#jaccard,dice 相似靠近1，不相似靠近0

def JaccardCoef(A, B):
    A, B = set(A), set(B)
    intersect = len(A.intersection(B))
    union = len(A.union(B))
    coef = try_divide(intersect, union)
    return coef

def DiceDist(A, B):
    A, B = set(A), set(B)
    intersect = len(A.intersection(B))
    union = len(A) + len(B)
    d = try_divide(2*intersect, union)
    return d

#返回1表示距离远，0表示相近
def computeDistance(A, B, dist="jaccard"):
    if dist == "jaccard":
        d = JaccardCoef(A, B)
    elif dist == "dice":
        d = DiceDist(A, B)
    else :
        d = 0
    d = 1-d
    return d


def main():

    ###############
    ## Load Data ##
    ###############
    ## load data
    inputPath = "./ModelSystem/Features/ngram"
    outputPath = "./ModelSystem/Features/distance"
    columnNames = ["query","title","description"]
    catagories = ["train","test"]
    ngram = ["unigram","bigram","trigram"]

    for cata in catagories:
        for colIndex in range(len(columnNames)):
            for igram in  ngram:

                path1 = "%s/%s_%s_%s.pickle" % (inputPath,columnNames[colIndex],igram,cata)
                colIndex2 = (colIndex+1) % (len(columnNames))
                path2 = "%s/%s_%s_%s.pickle" % (inputPath,columnNames[colIndex2],igram,cata)
                
                #加载两列的ngram
                with open(path1, "rb") as f:
                    data1 = pickle.load(f)

                with open(path2, "rb") as f:
                    data2 = pickle.load(f)

                sz = len(data1)
                dice = np.zeros([sz,1])
                jaccard = np.zeros([sz,1])
                #print(sz)
                for i in range(sz):
                    dice[i][0]=(computeDistance(data1[i],data2[i],dist="dice"))
                    jaccard[i][0]=(computeDistance(data1[i],data2[i],dist="jaccard"))
                    if(i<10):print(dice[i][0],jaccard[i][0])

                path1 = "%s/dice_%s_%s_%s_%s.pickle" % (outputPath,igram,columnNames[colIndex],columnNames[colIndex2],cata)

                path2 = "%s/jaccard_%s_%s_%s_%s.pickle" % (outputPath,igram,columnNames[colIndex],columnNames[colIndex2],cata)

                with open(path1, "wb") as f:
                    pickle.dump(dice,f)

                with open(path2, "wb") as f:
                    pickle.dump(jaccard,f)

                print("dis_%s_%s_%s_%s completed" % (igram,columnNames[colIndex],columnNames[colIndex2],cata))

    print("All Done.")




if __name__ == "__main__":
    main()
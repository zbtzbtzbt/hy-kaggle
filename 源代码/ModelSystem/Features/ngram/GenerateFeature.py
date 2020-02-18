
import pandas as pd
import pickle
import numpy as np
import scipy.sparse as sp

import re
import ngram


def main():

    ###############
    ## Load Data ##
    ###############
    ## load data
    dataPath = "./ModelSystem/ProcessedData"
    columnNames = ["query","title","description"]
    catagories = ["train","test"]

    
    for cata in catagories:
        for col in columnNames:
            path = "%s/%s_%s.pickle" % (dataPath,col,cata)           
            with open(path, "rb") as f:
                input = pickle.load(f)

            sz = len(input)
            #开始1,2,3元文法
            output_unigram = []
            output_bigram = []
            output_trigram = []
            for i in range(sz):
                text = str(input[i])
                #去除标点
                wordList = text.split()

                unigram = wordList
                bigram = ngram.getBigram(wordList, "_")
                trigram = ngram.getTrigram(wordList, "_")

                for i in range(len(unigram)):
                    if(unigram[i]=="nan"): unigram[i] = ""

                for i in range(len(bigram)):
                    if(bigram[i]=="nan"): bigram[i] = ""

                for i in range(len(trigram)):
                    if(trigram[i]=="nan"): trigram[i] = ""

                output_unigram.append(unigram)
                output_bigram.append(bigram)
                output_trigram.append(trigram)
            
                #print(unigram)
                #print(bigram)
                #print(trigram)
                #raise Exception("sdf")

            path = "./ModelSystem/Features/ngram/%s_unigram_%s.pickle" % (col,cata)    
            with open(path, "wb") as f:
                pickle.dump(output_unigram,f)

            path = "./ModelSystem/Features/ngram/%s_bigram_%s.pickle" % (col,cata)    
            with open(path, "wb") as f:
                pickle.dump(output_bigram,f)

            path = "./ModelSystem/Features/ngram/%s_trigram_%s.pickle" % (col,cata)    
            with open(path, "wb") as f:
                pickle.dump(output_trigram,f)

            print("%s_ngram_%s Completed" % (col,cata) )
    
   # ret = ngram.getBigram(x["query_unigram"], join_str)

    print("ngram All Done.")


def test():

    ###############
    ## Load Data ##
    ###############
    ## load data
    dataPath = "./ModelSystem/ProcessedData"
    columnNames = ["query","title","description"]
    catagories = ["train","test"]

    
    for cata in catagories:
        for col in columnNames:
            path = "%s/%s_%s.pickle" % (dataPath,col,cata)           
            with open(path, "rb") as f:
                input = pickle.load(f)

            sz = len(input)
            #开始1,2,3元文法
            output_unigram = []
            output_bigram = []
            output_trigram = []
            for i in range(2):
                text = input[i]
                #去除标点
                text = re.sub("[^0-9a-zA-Z.]"," ",text)
                wordList = text.split()

                unigram = wordList
                bigram = ngram.getBigram(wordList, "_")
                trigram = ngram.getTrigram(wordList, "_")

                print(unigram)
                print(bigram)
                print(trigram)
    
    
   # ret = ngram.getBigram(x["query_unigram"], join_str)

    print("ngram All Done.")

if __name__ == "__main__":
    main()

    #str = "123  23"
    #print(str.split())

    pass
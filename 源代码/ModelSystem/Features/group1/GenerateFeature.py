import pickle
import numpy as np
import pandas as pd
#import backports.lzma as lzma
import lzma
from difflib import SequenceMatcher as seq_matcher

folderPath = "./ModelSystem/Features/group1"
ngrams = ["unigram","bigram","trigram"]
features = ["quert","title","description"]
catagories = ["train","test"]
ngramFolderPath="./ModelSystem/Features/ngram"

#ratio of words from query that are present in title
def gen_ratio_word_query_in_title():
    for cata in catagories:

        with open("%s/query_unigram_%s.pickle" % (ngramFolderPath,cata),"rb") as f:
            query_unigram = pickle.load(f)

        with open("%s/title_unigram_%s.pickle" % (ngramFolderPath,cata),"rb") as f:
            title_unigram = pickle.load(f)

        sz = len(query_unigram)
        output = np.zeros([sz,1])
        
        for i in range(sz):
            cnt = 0
            for qword  in query_unigram[i]:
                for tword in title_unigram[i]:
                    lev_dist = seq_matcher(None,qword,tword).ratio()
                    if lev_dist > 0.9:
                        cnt += 1
                        
            cnt = cnt / len(query_unigram[i])
            output[i][0] = cnt
        
        print(output.shape)

        with open("%s/ratio_word_query_in_title_%s.pickle" % (folderPath,cata),"wb") as f:
            pickle.dump(output,f)

def gen_count_word_query_in_title():
    for cata in catagories:

        with open("%s/query_unigram_%s.pickle" % (ngramFolderPath,cata),"rb") as f:
            query_unigram = pickle.load(f)

        with open("%s/title_unigram_%s.pickle" % (ngramFolderPath,cata),"rb") as f:
            title_unigram = pickle.load(f)

        sz = len(query_unigram)
        output = np.zeros([sz,1])
        
        for i in range(sz):
            cnt = 0
            for qword  in query_unigram[i]:
                for tword in title_unigram[i]:
                    lev_dist = seq_matcher(None,qword,tword).ratio()
                    if lev_dist > 0.9:
                        cnt += 1
                        
            output[i][0] = cnt
        
        print(output.shape)

        with open("%s/count_word_query_in_title_%s.pickle" % (folderPath,cata),"wb") as f:
            pickle.dump(output,f)

#whether last word from query is present in title - boolean flag
def last_word_from_query_present_title():
    for cata in catagories:
        with open("%s/query_unigram_%s.pickle" % (ngramFolderPath,cata),"rb") as f:
            query_unigram = pickle.load(f)

        with open("%s/title_unigram_%s.pickle" % (ngramFolderPath,cata),"rb") as f:
            title_unigram = pickle.load(f)

        sz = len(query_unigram)
        output = np.zeros([sz,1])

        for i in range(sz):
            cnt = 0

            for word in title_unigram[i]:
                lev_dist = seq_matcher(None,query_unigram[i][-1],word).ratio()
                if lev_dist > 0.9: 
                    cnt = 1
                    break

            output[i][0] = cnt
        
        print(output.shape)

        with open("%s/last_word_from_query_present_title_%s.pickle" % (folderPath,cata),"wb") as f:
            pickle.dump(output,f)


#number of words in query
def number_of_words_in_query():
    for cata in catagories:

        with open("%s/query_unigram_%s.pickle" % (ngramFolderPath,cata),"rb") as f:
            query_unigram = pickle.load(f)

        sz = len(query_unigram)
        output = np.zeros([sz,1])
        
        for i in range(sz):
            output[i][0] = len(query_unigram[i])
        
        print(output[:10])
        with open("%s/number_of_words_in_query_%s.pickle" % (folderPath,cata),"wb") as f:
            pickle.dump(output,f)

def number_of_words_in_title():
    for cata in catagories:

        with open("%s/title_unigram_%s.pickle" % (ngramFolderPath,cata),"rb") as f:
            query_unigram = pickle.load(f)

        sz = len(query_unigram)
        output = np.zeros([sz,1])
        
        for i in range(sz):
            output[i][0] = len(query_unigram[i])
        
        #print(output[:10])
        with open("%s/number_of_words_in_title_%s.pickle" % (folderPath,cata),"wb") as f:
            pickle.dump(output,f)

def missing_indicator():
    for cata in catagories:
        data = pd.read_csv("./ModelSystem/RawData/%s.csv" % cata).fillna("")
        data = data["product_description"]
        data = list(data)

        sz = len(data)
        output = np.zeros([sz,1])

        for i in range(sz):
            if(data[i]==""):output[i][0]=1
        
        #print(output[:12])
        with open("%s/missing_indicator_%s.pickle" % (folderPath,cata),"wb") as f:
            pickle.dump(output,f)




def compressionDistance(x,y,l_x=None,l_y=None):
    if x==y:
        return 0
    x_b = x.encode('utf-8')
    y_b = y.encode('utf-8')
    if l_x is None:
        l_x = len(lzma.compress(x_b))
        l_y = len(lzma.compress(y_b))
    l_xy = len(lzma.compress(x_b+y_b))
    l_yx = len(lzma.compress(y_b+x_b))
    dist = (min(l_xy,l_yx)-min(l_x,l_y))/max(l_x,l_y)
    return dist

def distance_between_query_and_title():

    for cata in catagories:

        with open("%s/query_unigram_%s.pickle" % (ngramFolderPath,cata),"rb") as f:
            query_unigram = pickle.load(f)

        with open("%s/title_unigram_%s.pickle" % (ngramFolderPath,cata),"rb") as f:
            title_unigram = pickle.load(f)

        sz = len(query_unigram)

        compression_distance = np.zeros([sz,1])
        edit_distance = np.zeros([sz,1])
        mean_maximum_edit_distance = np.zeros([sz,1])
        
        for i in range(sz):
            query = " ".join(query_unigram[i])
            title = " ".join(title_unigram[i])
 
            compression_distance[i][0] = compressionDistance(query,title)
            edit_distance[i][0] = 1 - seq_matcher(None,query,title).ratio()
            
            lev_dist_arr = []
            for q in query.split():
                lev_dist_q = []
                for t in title.split():
                    lev_dist = seq_matcher(None,q,t).ratio()
                    lev_dist_q.append(lev_dist)
                lev_dist_arr.append(lev_dist_q)

            lev_max = 0
            for item in lev_dist_arr:
                lev_max_q = max(item)
                lev_max += lev_max_q
            lev_max = 1- lev_max/len(lev_dist_arr)
            mean_maximum_edit_distance[i][0] =  lev_max

            if(i%1000==0):print(i)
            
        with open("%s/compression_distance_%s.pickle" % (folderPath,cata),"wb") as f:
            pickle.dump(compression_distance,f)
        
        with open("%s/edit_distance_%s.pickle" % (folderPath,cata),"wb") as f:
            pickle.dump(edit_distance,f)
        
        with open("%s/mean_maximum_edit_distance_%s.pickle" % (folderPath,cata),"wb") as f:
            pickle.dump(mean_maximum_edit_distance,f)


if __name__ == "__main__":
    gen_ratio_word_query_in_title()
    gen_count_word_query_in_title()
    last_word_from_query_present_title()
    number_of_words_in_query()
    number_of_words_in_title()
    missing_indicator()
    distance_between_query_and_title() #3
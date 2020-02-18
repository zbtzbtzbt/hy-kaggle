import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

from sklearn.feature_extraction import text
from difflib import SequenceMatcher as seq_matcher
from itertools import combinations_with_replacement
from sklearn.preprocessing import MinMaxScaler
import re
import lzma
from collections import Counter
import pickle

def construct_extended_query(queries,queries_test,titles,titles_test,top_words=10):
    y = pd.read_csv('./ModelSystem/RawData/train.csv').median_relevance.values
    
    stop_words = text.ENGLISH_STOP_WORDS
    pattern = re.compile(r'\b(' + r'|'.join(stop_words) + r')\b\s*')
    
    train = pd.read_csv('./ModelSystem/RawData/train.csv')
    test = pd.read_csv('./ModelSystem/RawData/test.csv')
    
    data = []
    query_ext_train = np.zeros(len(train)).astype(np.object)
    query_ext_test = np.zeros(len(test)).astype(np.object)

    for q in np.unique(queries):
        #print (q)
        q_mask = queries == q
        #print(q_mask[:100])
        #exit()
        q_test = queries_test == q
        
        #抽取某一query的所有产品
        titles_q = titles[q_mask]
        y_q = y[q_mask]
        
        good_mask = y_q > 3
        #抽取产品中相关度为4的产品title
        titles_good = titles_q[good_mask]
        ext_q = str(q)
        for item in titles_good:
            ext_q += ' '+str(item)
        #替换停用词
        ext_q = pattern.sub('', ext_q)
        #选出title中出现频数最高的10个词语
        c = [word for word, it in Counter(ext_q.split()).most_common(top_words)]
        c = ' '.join(c)
        data.append([q,ext_q,c])
        query_ext_train[q_mask] = c
        query_ext_test[q_test] = c
    
    train['query'] = query_ext_train
    test['query'] = query_ext_test
    train['product_title'] = titles
    test['product_title'] = titles_test

    return train, test

def compression_distance(x,y,l_x=None,l_y=None):
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

def assemble_counts2(train):
    X = []
    queries = []
    
    for i in range(len(train.id)):
        query = train['query'][i]
        title = train.product_title[i]
        
        dist_qt = compression_distance(query,title)
        dist_qt2 = 1 - seq_matcher(None,query,title).ratio()
        
        query_len = len(query.split())
        
        lev_dist_arr = []
        word_rank_list = []
        word_q_ind = 0
        word_counter_qt = 0
        for q in query.split():
            word_q_ind += 1
            lev_dist_q = []
            for t in title.split():
                lev_dist = seq_matcher(None,q,t).ratio()
                if lev_dist > 0.9:
                    word_counter_qt += 1
                    word_rank_list.append(word_q_ind)
                    #tmp_title += ' '+q # add such words to title to increase their weights in tfidf
                lev_dist_q.append(lev_dist)
            lev_dist_arr.append(lev_dist_q)
        if word_counter_qt == 0:
            maxrank = 0
        else:
            maxrank = 26 - min(word_rank_list)
        
        
        lev_max = 0
        for item in lev_dist_arr:
            lev_max_q = max(item)
            lev_max += lev_max_q
        lev_max = 1- lev_max/len(lev_dist_arr)
        word_counter_qt_norm = word_counter_qt/query_len
        
        
        X.append([word_counter_qt,dist_qt,dist_qt2,lev_max,word_counter_qt_norm,maxrank])
        queries.append(query)

    X = np.array(X).astype(np.float)

    return X, np.array(queries)

def generateFeatures():
#Extended queries top 10 words
    with open("./ModelSystem/ProcessedData/query_train.pickle" ,"rb") as f:
        queries = pickle.load(f)
        queries = np.array(queries)

    with open("./ModelSystem/ProcessedData/query_test.pickle" ,"rb") as f:
        queries_test = pickle.load(f)
        queries_test = np.array(queries_test)

    with open("./ModelSystem/ProcessedData/title_train.pickle" ,"rb") as f:
        titles = pickle.load(f)
        titles = np.array(titles)

    with open("./ModelSystem/ProcessedData/title_test.pickle" ,"rb") as f:
        titles_test = pickle.load(f)
        titles_test = np.array(titles_test)

    print(queries[0])
    #return
    
    train_ext, test_ext = construct_extended_query(queries,queries_test,titles,titles_test,top_words=10)


    X5, queries_ext = assemble_counts2(train_ext.fillna(""))
    X5_test, queries_ext_test = assemble_counts2(test_ext.fillna(""))

    
    with open("./ModelSystem/Features/group2/X5_train.pickle" ,"wb") as f:
        pickle.dump(X5,f)

    with open("./ModelSystem/Features/group2/queries_ext.pickle" ,"wb") as f:
        pickle.dump(queries_ext,f)

    with open("./ModelSystem/Features/group2/X5_test.pickle" ,"wb") as f:
        pickle.dump(X5_test,f)

    with open("./ModelSystem/Features/group2/queries_ext_test.pickle" ,"wb") as f:
        pickle.dump(queries_ext_test,f)

    

    np.savetxt("./ModelSystem/Features/group2/" + 'train_ext_counts_top10.txt',X5)
    np.savetxt("./ModelSystem/Features/group2/" + 'test_ext_counts_top10.txt',X5_test)

    print(X5.shape)

    
    tmp = pd.DataFrame(train_ext,columns=['id','query','product_title','product_description','median_relevance','relevance_variance'])
    tmp.to_csv("./ModelSystem/Features/group2/" + 'train_ext_top10.csv',index=False)
    tmp = pd.DataFrame(test_ext,columns=['id','query','product_title','product_description'])
    tmp.to_csv("./ModelSystem/Features/group2/" +  'test_ext_top10.csv',index=False)
    

generateFeatures()
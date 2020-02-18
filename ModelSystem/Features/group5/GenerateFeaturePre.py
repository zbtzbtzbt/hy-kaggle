#import cfg
import pandas as pd
import numpy as np
import scipy.sparse as sp
import re
import  pickle

from bs4 import BeautifulSoup
#from nltk.stem.porter import *
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import wordnet

from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics import pairwise_distances

from sklearn.manifold import TSNE

#from tsne import bh_sne
#先 group5 再 group4

from gensim.models import Word2Vec

print("Feature extractor (Mikhail's part)")
print('** see cfg.py for path settings **')

path_w2v_pretrained_model = './ModelSystem/Features/w2v/GoogleNews-vectors-negative300.bin'
print('\t load pretrained model from {}'.format(path_w2v_pretrained_model))
import gensim
embedder = gensim.models.KeyedVectors.load_word2vec_format(path_w2v_pretrained_model, binary=True)

#load data
print('Reading data')
train_df = pd.read_csv('./ModelSystem/ProcessedData/train.csv' , encoding='utf-8').fillna('')
test_df  = pd.read_csv('./ModelSystem/ProcessedData/test.csv', encoding='utf-8').fillna('')


#########################
###  Lemmatizing part ###
#########################

print('Lemmatizing')
toker = TreebankWordTokenizer()
lemmer = wordnet.WordNetLemmatizer()

def text_preprocessor(x):
    '''
    Get one string and clean\lemm it
    '''
    tmp = x#.unicode(x) #unicode(x)
    tmp = tmp.lower().replace('blu-ray', 'bluray').replace('wi-fi', 'wifi')
    x_cleaned = tmp.replace('/', ' ').replace('-', ' ').replace('"', '')
    tokens = toker.tokenize(x_cleaned)
    return " ".join([lemmer.lemmatize(z) for z in tokens])

# lemm query
train_df['query_stem'] = train_df['query'].apply(text_preprocessor)
test_df[ 'query_stem'] =  test_df['query'].apply(text_preprocessor)
# lemm description
train_df['desc_stem']  = train_df['product_description'].apply(text_preprocessor)
test_df[ 'desc_stem']  =  test_df['product_description'].apply(text_preprocessor)
# lemm title
train_df['title_stem'] = train_df['product_title'].apply(text_preprocessor)
test_df[ 'title_stem'] =  test_df['product_title'].apply(text_preprocessor)

#OK

####################
### Similarities ###
####################

print('Calc similarities')

def calc_cosine_dist(text_a ,text_b, vect):
    return pairwise_distances(vect.transform([text_a]), vect.transform([text_b]), metric='cosine')[0][0]

def calc_set_intersection(text_a, text_b):
    a = set(text_a.split())
    b = set(text_b.split())
    return len(a.intersection(b)) *1.0 / len(a)

# vectorizers for similarities
print('\t fit vectorizers')
tfv_orig = TfidfVectorizer(ngram_range=(1,2), min_df=2)
tfv_stem = TfidfVectorizer(ngram_range=(1,2), min_df=2)
tfv_desc = TfidfVectorizer(ngram_range=(1,2), min_df=2)
tfv_orig.fit(
    list(train_df['query'].values) + 
    list(test_df['query'].values) + 
    list(train_df['product_title'].values) + 
    list(test_df['product_title'].values)
) 
tfv_stem.fit(
    list(train_df['query_stem'].values) + 
    list(test_df['query_stem'].values) + 
    list(train_df['title_stem'].values) + 
    list(test_df['title_stem'].values)
) 
tfv_desc.fit(
    list(train_df['query_stem'].values) + 
    list(test_df['query_stem'].values) + 
    list(train_df['desc_stem'].values) + 
    list(test_df['desc_stem'].values)
) 

# for train
print('\t process train')
cosine_orig = []
cosine_stem = []
cosine_desc = []
set_stem = []
for i, row in train_df.iterrows():
    cosine_orig.append(calc_cosine_dist(row['query'], row['product_title'], tfv_orig))
    cosine_stem.append(calc_cosine_dist(row['query_stem'], row['title_stem'], tfv_stem))
    cosine_desc.append(calc_cosine_dist(row['query_stem'], row['desc_stem'], tfv_desc))
    set_stem.append(calc_set_intersection(row['query_stem'], row['title_stem']))
train_df['cosine_qt_orig'] = cosine_orig
train_df['cosine_qt_stem'] = cosine_stem
train_df['cosine_qd_stem'] = cosine_desc
train_df['set_qt_stem'] = set_stem   

# for test
print('\t process test')
cosine_orig = []
cosine_stem = []
cosine_desc = []
set_stem = []
for i, row in test_df.iterrows():
    cosine_orig.append(calc_cosine_dist(row['query'], row['product_title'], tfv_orig))
    cosine_stem.append(calc_cosine_dist(row['query_stem'], row['title_stem'], tfv_stem))
    cosine_desc.append(calc_cosine_dist(row['query_stem'], row['desc_stem'], tfv_desc))
    set_stem.append(calc_set_intersection(row['query_stem'], row['title_stem']))
test_df['cosine_qt_orig'] = cosine_orig
test_df['cosine_qt_stem'] = cosine_stem
test_df['cosine_qd_stem'] = cosine_desc
test_df['set_qt_stem'] = set_stem  



################
### w2v part ###
################

print('w2v part')

def calc_w2v_sim(row):
    '''
    Calc w2v similarities and diff of centers of query\title
    '''
    a2 = [x for x in row['query_stem'].lower().split() if x in embedder.vocab]
    b2 = [x for x in row['title_stem'].lower().split() if x in embedder.vocab]

    if len(a2)>0 and len(b2)>0:
        w2v_sim = embedder.n_similarity(a2, b2)
    else:
        return((-1, -1, np.zeros(300)))
    
    vectorA = np.zeros(300)
    for w in a2:
        vectorA += embedder[w]
    vectorA /= len(a2)

    vectorB = np.zeros(300)
    for w in b2:
        vectorB += embedder[w]
    vectorB /= len(b2)

    vector_diff = (vectorA - vectorB)

    w2v_vdiff_dist = np.sqrt(np.sum(vector_diff**2))
    return (w2v_sim, w2v_vdiff_dist, vector_diff)



# for train
print('\t process train')
X_w2v = []
sim_list = []
dist_list = []
for i,row in train_df.iterrows():
    sim, dist, vdiff = calc_w2v_sim(row)
    X_w2v.append(vdiff)
    sim_list.append(sim)
    dist_list.append(dist)
X_w2v_tr = np.array(X_w2v)
train_df['w2v_sim'] = np.array(sim_list)
train_df['w2v_dist'] = np.array(dist_list)

# for test
print('\t process test')
X_w2v = []
sim_list = []
dist_list = []
for i,row in test_df.iterrows():
    sim, dist, vdiff = calc_w2v_sim(row)
    X_w2v.append(vdiff)
    sim_list.append(sim)
    dist_list.append(dist)
X_w2v_te = np.array(X_w2v)
test_df['w2v_sim'] = np.array(sim_list)
test_df['w2v_dist'] = np.array(dist_list)

print('\t dump w2v-features')
pickle.dump((X_w2v_tr, X_w2v_te), open("./ModelSystem/Features/group5/" + 'X_w2v.pickle', 'wb'), protocol=2)



#####################
### tSNE features ###
#####################

print('tSNE part')
print('\t [1\3] process title')
vect = TfidfVectorizer(ngram_range=(1,2), min_df=3)
X_tf = vect.fit_transform(list(train_df['title_stem'].values) + list(test_df['title_stem'].values))
svd = TruncatedSVD(n_components=200)
X_svd = svd.fit_transform(X_tf)
X_scaled = StandardScaler().fit_transform(X_svd)

#X_tsne = bh_sne(X_scaled)
X_tsne = TSNE(n_components=2, random_state=0)
X_tsne = X_tsne.fit_transform(X_scaled)

train_df['tsne_title_1'] = X_tsne[:len(train_df), 0]
train_df['tsne_title_2'] = X_tsne[:len(train_df), 1]
test_df[ 'tsne_title_1'] = X_tsne[len(train_df):, 0]
test_df[ 'tsne_title_2'] = X_tsne[len(train_df):, 1]

print('\t [2\3] process title-query')
vect = TfidfVectorizer(ngram_range=(1,2), min_df=3)
X_title = vect.fit_transform(list(train_df['title_stem'].values) + list(test_df['title_stem'].values))
X_query = vect.fit_transform(list(train_df['query_stem'].values) + list(test_df['query_stem'].values))
X_tf = sp.hstack([X_title, X_query]).tocsr()
svd = TruncatedSVD(n_components=200)
X_svd = svd.fit_transform(X_tf)
X_scaled = StandardScaler().fit_transform(X_svd)

#X_tsne = bh_sne(X_scaled)
X_tsne = TSNE(n_components=2, random_state=0)
X_tsne = X_tsne.fit_transform(X_scaled)

train_df['tsne_qt_1'] = X_tsne[:len(train_df), 0]
train_df['tsne_qt_2'] = X_tsne[:len(train_df), 1]
test_df[ 'tsne_qt_1'] = X_tsne[len(train_df):, 0]
test_df[ 'tsne_qt_2'] = X_tsne[len(train_df):, 1]

print('\t [3\3] process description')
vect = TfidfVectorizer(ngram_range=(1,2), min_df=3)
X_desc = vect.fit_transform(list(train_df['desc_stem'].values) + list(test_df['desc_stem'].values))
X_tf = X_desc
svd = TruncatedSVD(n_components=200)
X_svd = svd.fit_transform(X_tf)
X_scaled = StandardScaler().fit_transform(X_svd)

#X_tsne = bh_sne(X_scaled)
X_tsne = TSNE(n_components=2, random_state=0)
X_tsne = X_tsne.fit_transform(X_scaled)

train_df['tsne_desc_1'] = X_tsne[:len(train_df), 0]
train_df['tsne_desc_2'] = X_tsne[:len(train_df), 1]
test_df[ 'tsne_desc_1'] = X_tsne[len(train_df):, 0]
test_df[ 'tsne_desc_2'] = X_tsne[len(train_df):, 1]

print('\t dump results')
train_df.to_pickle("./ModelSystem/Features/group5/" + 'train_df.pickle')
test_df.to_pickle( "./ModelSystem/Features/group5/"+ 'test_df.pickle')



####################
### X_additional ###
####################
print("Dump additional features")
feat_list = [
    u'w2v_sim',
    u'w2v_dist',
    u'tsne_title_1', 
    u'tsne_title_2', 
    u'tsne_qt_1',
    u'tsne_qt_2',
    u'cosine_qt_orig', 
    u'cosine_qt_stem', 
    u'cosine_qd_stem',
    u'set_qt_stem'
]
X_additional_tr = train_df[feat_list].as_matrix()
X_additional_te = test_df[feat_list].as_matrix()

np.savetxt("./ModelSystem/Features/group5/" + 'X_additional_tr.txt', X_additional_tr)
np.savetxt("./ModelSystem/Features/group5/" + 'X_additional_te.txt', X_additional_te)

print('Done!')
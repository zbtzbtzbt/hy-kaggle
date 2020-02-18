import pandas as pd
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
import pickle



def textCleaning(raw_text,remove_stopwords=False,\
    remove_number=False,remove_punctuation=False,\
        remove_HTMLtags=True):
    '''
    process the raw text(string) and return the processed text(string)
    remove the numbers,punctuations ,etc. from the text
    '''
    #remove HTML tags
    processed_text = str(raw_text)
    if(remove_HTMLtags):
        processed_text = BeautifulSoup(processed_text).get_text()

    #remove \n \r \\ \ and so on
    processed_text  = re.sub(r"\\[a-z]"," ",processed_text)
    processed_text = re.sub(r'\\\\' , r'\\' ,processed_text)
    processed_text = re.sub(r"\\\"","\"",processed_text)
    processed_text = re.sub(r'\\\'' , '\'' ,processed_text)

    #remove number
    if(remove_number):
        processed_text = re.sub("[0-9]"," ",processed_text)
    
    if(remove_punctuation):
        processed_text = re.sub("[^0-9a-zA-Z]"," ",processed_text)

    processed_text = processed_text.lower()
    words = processed_text.split()

    #get the stop word
    #nltk.download() #you need to execute this code to download the dataset containing "stop words",
    #but i will upload this dataset to QQ group   (HY)
    meaningful_words=words
    if(remove_stopwords):
        stop_words = set(stopwords.words("english") )
        meaningful_words = [w for w in words if not w in stop_words]

    processed_text =" ".join(meaningful_words)
 
    return processed_text


def generateCorpus():
    
    with open("./ModelSystem/ProcessedData/query_train.pickle","rb") as f:
        query_train = pickle.load(f)
     
    with open("./ModelSystem/ProcessedData/title_train.pickle","rb") as f:
        title_train = pickle.load(f)
    
    with open("./ModelSystem/ProcessedData/description_train.pickle","rb") as f:
        description_train = pickle.load(f)

    with open("./ModelSystem/ProcessedData/query_test.pickle","rb") as f:
        query_test = pickle.load(f)

    with open("./ModelSystem/ProcessedData/title_test.pickle","rb") as f:
        title_test = pickle.load(f)

    with open("./ModelSystem/ProcessedData/description_test.pickle","rb") as f:
        description_test = pickle.load(f)


    corpus = []

    trainDataSz = len(query_train)

    testDataSz = len(query_test)

    print(trainDataSz)
    print(testDataSz)

    #=============================
    #print(query_train[:5])
    

    for i in range(trainDataSz):
        corpus.append(str(query_train[i]))
        corpus.append(str(title_train[i]))
        corpus.append(str(description_train[i]))
        if(i % 1000==0):
            print(i)

    for i in range(testDataSz):
        corpus.append(str(query_test[i]))
        corpus.append(str(title_test[i]))
        corpus.append(str(description_test[i]))
        if(i % 1000==0):
            print(i)

    #print(type(corpus))
    #print(type(corpus[0]))

    '''
    file = open("./ModelSystem/Features/tfidf/"+ "query_train.pickle","wb")
    pickle.dump(query_train,file)
    file.close()

    file = open("./ModelSystem/Features/tfidf/"+ "productTitle_train.pickle","wb")
    pickle.dump(productTitle_train,file)
    file.close()

    file = open("./ModelSystem/Features/tfidf/"+ "productDescription_train.pickle","wb")
    pickle.dump(productDescription_train,file)
    file.close()

    file = open("./ModelSystem/Features/tfidf/"+ "query_test.pickle","wb")
    pickle.dump(query_test,file)
    file.close()

    file = open("./ModelSystem/Features/tfidf/"+ "productTitle_test.pickle","wb")
    pickle.dump(productTitle_test,file)
    file.close()

    file = open("./ModelSystem/Features/tfidf/"+ "productDescription_test.pickle","wb")
    pickle.dump(productDescription_test,file)
    file.close()
    '''

    file = open("./ModelSystem/Features/tfidf/"+ "corpus.pickle","wb")
    pickle.dump(corpus,file)
    file.close()

max_features = 50000

def generateTFIDFSparseMatrix():   
    
    file = open("./ModelSystem/Features/tfidf/"+ "corpus.pickle","rb")
    corpus = pickle.load(file)
    file.close()

    from sklearn.feature_extraction.text import TfidfVectorizer

    vectorizer = TfidfVectorizer(min_df=3, # 最小支持度为2
        max_df=0.75,
        #max_features=max_features,
        strip_accents='unicode',
        analyzer='word',
        token_pattern=r"(?u)\b\w\w+\b",
        ngram_range=(1, 3),  # 二元文法模型
        use_idf=1,
        smooth_idf=1,
        sublinear_tf=1,
        #stop_words = 'english'
        stop_words = 'english'
        ) 

    '''
    tfidf__norm = "l2"
tfidf__max_df = 0.75
tfidf__min_df = 3
    '''

    #min_fd
    #7 74k
    #8 63k
    #10 47k

    tfidf = vectorizer.fit_transform(corpus)
    print(tfidf.shape)
    file = open("./ModelSystem/Features/tfidf/"+ "tfidfSparseMatrix.pickle","wb")
    pickle.dump(tfidf,file)
    file.close()
    
def main():
    generateCorpus()
    generateTFIDFSparseMatrix()
    pass
    

if __name__ == "__main__":
    main()

    



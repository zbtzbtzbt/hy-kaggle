import pandas as pd
from bs4 import BeautifulSoup
import re
import csv
import nltk
from nltk.corpus import stopwords
import nltk.stem
from nltk.stem import wordnet

lemmer = wordnet.WordNetLemmatizer()

replace_dict = {
    "nutri system": "nutrisystem",
    "soda stream": "sodastream",
    "playstation's": "ps",
    "playstations": "ps",
    "playstation": "ps",
    "(ps 2)": "ps2",
    "(ps 3)": "ps3",
    "(ps 4)": "ps4",
    "ps 2": "ps2",
    "ps 3": "ps3",
    "ps 4": "ps4",
    "coffeemaker": "coffee maker",
    "k-cups": "k cup",
    "k-cup": "k cup",
    "4-ounce": "4 ounce",
    "8-ounce": "8 ounce",
    "12-ounce": "12 ounce",
    "ounce": "oz",
    "button-down": "button down",
    "doctor who": "dr who",
    "2-drawer": "2 drawer",
    "3-drawer": "3 drawer",
    "in-drawer": "in drawer",
    "hardisk": "hard drive",
    "hard disk": "hard drive",
    "harley-davidson": "harley davidson",
    "harleydavidson": "harley davidson",
    "e-reader": "ereader",
    "levi strauss": "levi",
    "levis": "levi",
    "mac book": "macbook",
    "micro-usb": "micro usb",
    "screen protector for samsung": "screen protector samsung",
    "video games": "videogames",
    "game pad": "gamepad",
    "western digital": "wd",
    "eau de toilette": "perfume",
}
##########################
## Synonym Replacement ##
##########################
class WordReplacer(object):
    def __init__(self, word_map):
        self.word_map = word_map
    def replace(self, word):
        return [self.word_map.get(w, w) for w in word]


class CsvWordReplacer(WordReplacer):
    def __init__(self, fname):
        word_map = {}
        for line in csv.reader(open(fname)):
            word, syn = line
            if word.startswith("#"):
                continue
            word_map[word] = syn
        super(CsvWordReplacer, self).__init__(word_map)

replacer = CsvWordReplacer('./ModelSystem/RawData/synonyms.csv')
######################################################
dfTrain =pd.read_csv('./ModelSystem/RawData/train.csv')
dfTest = pd.read_csv('./ModelSystem//RawData/test.csv')

names = ["query", "product_title", "product_description"]
columns = ['id','query','product_title','product_description']
s = nltk.stem.SnowballStemmer('english')
leng=dfTrain.shape[0]
Id=[x for x in range(10158)]
mes=[]



def cleanText(l):
    l = BeautifulSoup(l).get_text()#html tag
    l=l.lower()# lower
    '''
    l = re.sub(r"\\[a-z]"," ",l)
    l = re.sub(r'\\\\' , r'\\' ,l)
    l= re.sub(r"\\\"","\"",l)
    l = re.sub(r'\\\'' , '\'' ,l)
    '''
    #######
    l = re.sub(r"[^0-9a-zA-Z ,.'\n]","",l)
    #l = re.sub(r"\n+"," ",l)
    #l = re.sub(r"\.+"," ",l)
    l = re.sub(r"\.+|\n+| +|,"," ",l)
    #######

    
    ## replace gb
    for vol in [16, 32, 64, 128, 500]:
        l = re.sub("%d gb"%vol, "%dgb"%vol, l)
        l = re.sub("%d g"%vol, "%dgb"%vol, l)
        l = re.sub("%dg "%vol, "%dgb "%vol, l)
    ## replace tb
    for vol in [2]:
        l = re.sub("%d tb"%vol, "%dtb"%vol, l)
    ## replace other words
    for k,v in replace_dict.items():
        l = re.sub(k, v, l)
    l = l.split()
    ## replace synonyms
    l = replacer.replace(l)
    #l = " ".join(l)
    #print(type(l))
    cleaned_text = [lemmer.lemmatize(ws) for ws in l]
    #return " ".join([lemmer.lemmatize(z) for z in tokens])
    #cleaned_text = [s.stem(ws) for ws in l]
    cleaned_text = " ".join(cleaned_text)
    if(cleaned_text=="nan"):cleaned_text=""
    
    return cleaned_text


def cleanTrain():
#train.csv
    for name in names:
        for i in range(leng):
            if(i%1000 == 0):print("i",i)
            l = dfTrain[name][i]
            l=str(l)
            
            dfTrain[name][i] = cleanText(l)

    dfTrain.to_csv("./ModelSystem/ProcessedData/train.csv")

#test.csv
def cleanTest():
    leng2=dfTest.shape[0]
    for name in names:
        for j in range(leng2):
            if(j %1000 == 0):print("j",j)
            h = dfTest[name][j]
            h=str(h)
            
            dfTest[name][j] = cleanText(h) 


    dfTest.to_csv("./ModelSystem/ProcessedData/test.csv")


cleanTrain()
cleanTest()



def cleanText_sim(l):
    l = BeautifulSoup(l).get_text()#html tag
    #l=l.lower()# lower
    '''
    l = re.sub(r"\\[a-z]"," ",l)
    l = re.sub(r'\\\\' , r'\\' ,l)
    l= re.sub(r"\\\"","\"",l)
    l = re.sub(r'\\\'' , '\'' ,l)
    '''
    #######
    l = re.sub(r"[^0-9a-zA-Z ,.'\"\n]","",l)
    #l = re.sub(r"\n+"," ",l)
    #l = re.sub(r"\.+"," ",l)
    l = re.sub(r"\n+",r"\n",l)
    l=re.sub(r" +"," ",l)
    #######

    
    ## replace gb
    for vol in [16, 32, 64, 128, 500]:
        l = re.sub("%d gb"%vol, "%dgb"%vol, l)
        l = re.sub("%d g"%vol, "%dgb"%vol, l)
        l = re.sub("%dg "%vol, "%dgb "%vol, l)
    ## replace tb
    for vol in [2]:
        l = re.sub("%d tb"%vol, "%dtb"%vol, l)
    ## replace other words
    for k,v in replace_dict.items():
        l = re.sub(k, v, l)
    l = l.split()
    ## replace synonyms
    l = replacer.replace(l)
    #l = " ".join(l)
    #print(type(l))
    cleaned_text = " ".join(l)
    #cleaned_text = l
    if(cleaned_text=="nan"):cleaned_text=""
    
    return cleaned_text
'''

leng2=dfTest.shape[0]
for name in names:
    for j in range(leng2):
        if(j %1000 == 0):print("j",j)
        h = dfTest[name][j]
        h=str(h)
        
        dfTest[name][j] = cleanText_sim(h) 

dfTest.to_csv("./SearchSystem/data/database.csv")
'''


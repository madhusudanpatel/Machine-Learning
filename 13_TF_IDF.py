
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import  PorterStemmer

ps=PorterStemmer()

sentence=pd.read_csv(r"D:\AI_With _Python\10_Machine_Learning\SMSSpamCollection.csv",sep='\t', names=["label", "message"])
print(sentence)

corpus=[]

for i in range (0,len(sentence)):
    review=re.sub('[^a-zA-z]',' ',sentence['message'][i])
    reviwe=review.lower().split()
    reviwe=[ps.stem(word) for word in reviwe if not word in stopwords.words('english')]
    reviwe=" ".join(reviwe)
    corpus.append(reviwe)

print(corpus)    

#...............................................Create Bag Of Words..........................................

# from sklearn.feature_extraction.text import CountVectorizer
# tfidf=CountVectorizer(max_features=100,binary=True)
# X=tfidf.fit_transform(corpus).toarray()

# print(X)

import numpy as np
np.set_printoptions(edgeitems=30,linewidth=10000,formatter=dict(float=lambda x: "%.3g"%x))
# print(X)


#.....................................................TF_IDF       NLP.....................................

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer(max_features=100,binary=True)
X=tfidf.fit_transform(corpus).toarray()

print("--------UNIGRAM--------",X)

print(tfidf.vocabulary_)

tfidf=TfidfVectorizer(max_features=100,binary=True,ngram_range=(2,3))
X=tfidf.fit_transform(corpus).toarray()

print(tfidf.vocabulary_)
print("----------BIGRAM------TRIGRAM------------",X)
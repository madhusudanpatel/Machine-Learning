

message="""This project would not have been possible without the combined support.
encouragement, and guidance of all the above-mentioned individuals and groups."""

import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps=PorterStemmer()
corpus=[]
sentence=pd.DataFrame([message],columns=['sentence'])
print(sentence)
corpus=[]
for i in range(0,len(sentence)):
    review=re.sub('[^a-zA-z]',' ',sentence['sentence'][i])
    review=review.lower().split()
    
    review=[ps.stem(word) for word in review if not word in stopwords.words('english')]
    review=' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer(max_features=5,binary=True)
X=cv.fit_transform(corpus).toarray()

print(X)
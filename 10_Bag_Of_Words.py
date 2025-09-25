import pandas as pd

# If your file is in the same folder as your script
messages = pd.read_csv(r"D:\AI_With _Python\10_Machine_Learning\SMSSpamCollection.csv", sep='\t', names=["label", "message"])

print(messages.head())

## Data Cleaning And Preprocessing
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

corpus=[]
for i in range(0,len(messages)):
    review=re.sub('[^a-zA-z]',' ',messages['message'][i])
    # print(review)
    review=review.lower()
    review=review.split()
    review=[ps.stem(word) for word in review if not word in stopwords.words('english')]
    review=' '.join(review)
    corpus.append(review)
    
# print("\n",corpus)    


#........................................Create Bag Of Words
## .....................Create the Bag OF Words model

from sklearn.feature_extraction.text import CountVectorizer
## for Binary BOW enable binary=True
cv=CountVectorizer(max_features=100,binary=True)
X=cv.fit_transform(corpus).toarray()

# import numpy as np
# np.set_printoptions(edgeitems=30, linewidth=100000, 
#     formatter=dict(float=lambda x: "%.3g" % x))

print(X)
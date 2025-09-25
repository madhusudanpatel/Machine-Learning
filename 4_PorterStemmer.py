

from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
ps =PorterStemmer()
lemma=WordNetLemmatizer()

example_words=["program","programing","programer","programs","programmed"]

#.......................................Perfrom Stemming............................

for word in example_words:
    # print("{0:20}{1:20}".format(word,ps.stem(word)))
    print("{0:20}{1:20}".format(word,lemma.lemmatize(word,pos='v')))
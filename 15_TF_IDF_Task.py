

corpus = ['data science is one of the most important fields of science',
            'this is one of the best data science courses',
            'data scientists analyze data' ]


# # word_count=[len(sentence.split()) for sentence in corpus ]
# # # print(word_count)
# # # #....................................Total - words..............................
# # words="  ".join(corpus).split()
# # print(words)
# # print(" Lenght ",len(words))
# # #......................................Word-length.............................
# # word_length={word :len(word) for word in set(words)}

# # print(word_length)
# # print(" Lenght ",len(word_length))

# # #........................................................................................

# word_set=set()

# # # words =[doc.split() for doc in corpus]

# # # word_set=word_set.union(set(word_length))

# # print("Number of word in the Corpus :",len(word_set))
# # print("The word in the corpus :\n",word_set)


# #..........................................Arrange all words in dataFram..............................

words_set = set()

for doc in  corpus:
    words = doc.split(' ')
    words_set = words_set.union(set(words))
    
print('Number of words in the corpus:',len(words_set))
print('The words in the corpus: \n', words_set)

import pandas as pd
import numpy as np
n_docs = len(corpus)         #·Number of documents in the corpus
n_words_set = len(words_set) #·Number of unique words in the 

df_tf = pd.DataFrame(np.zeros((n_docs, n_words_set)), columns=list(words_set))

# Compute Term Frequency (TF)
for i in range(n_docs):
    words = corpus[i].split(' ') # data science is one of the most important fields of science
    for w in words:
        df_tf[w][i] = df_tf[w][i] + (1 / len(words))
        
print(df_tf)

# #..........................................................................


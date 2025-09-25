
#.....................................Corpus...........................................

corpus="""
hello Welcome to Sunny's   NLP Classes.
Please do complete entire course ! to become expert in NLP."""


#......................................Tokenization...................................

##.............Paragraphs --> Sentences [Corpus -->Document]....................

#..............import sent_tokenize Libaraty

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Tokenizing sentences
sentences = sent_tokenize(corpus)

# Printing the result
print(sentences)
print(type(sentences))
# print(sentences[1])

#......................Paragraph.................
for paragraph in sentences:
    print((paragraph))
    



#.....................................Tokenization 
#                                                  Sentence --> words [Documents -->Words] 
                                                     

from nltk.tokenize import word_tokenize

# Tokenizing sentences
words = word_tokenize(corpus)

# # Printing the result
print(words) 
# print(type(words)) 
  
# for sentences in paragraph:
#     print(word_tokenize(sentences))
    

#.......................................wordpunct_Tokenization.......................
from nltk.tokenize import wordpunct_tokenize  
print(wordpunct_tokenize(corpus))


#.......................................Treebank_tokenzition.............................

from nltk.tokenize import TreebankWordTokenizer

tokenizerr=TreebankWordTokenizer()
print(tokenizerr.tokenize(corpus))
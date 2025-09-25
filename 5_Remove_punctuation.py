

import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
example_sentence = """Python programmers often tend like programming in python because it's 
               like english. We call people who program in python pythonistas."""
# Remove punctuation 
example_sentence_no_punct = example_sentence.translate(str.maketrans("", "",string.punctuation)) 

word_tokens = word_tokenize(example_sentence_no_punct) 
lemmetizer=WordNetLemmatizer()
# Perform lemmatization 
print("{0:20}{1:20}".format("--Word--","--Lemma--")) 
for word in word_tokens: 
   print("{0:20}{1:20}".format(word, lemmetizer.lemmatize(word, pos="v")))





#...............................................................................................................

# import string
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer

# # Example sentence
# example_sentence = """Python programmers often tend like programming in python because it's 
#                like english. We call people who program in python pythonistas."""

# # 1. Remove punctuation
# example_sentence_no_punct = example_sentence.translate(str.maketrans("", "", string.punctuation))

# # 2. Tokenize sentence into words
# word_tokens = word_tokenize(example_sentence_no_punct)

# # 3. Initialize Lemmatizer
# lemmatizer = WordNetLemmatizer()

# # 4. Print results
# print("{0:20}{1:20}{2:20}".format("--Word--", "--Lemma (Noun)--", "--Lemma (Verb)--"))
# print("-" * 60)
# for word in word_tokens:
#     lemma_noun = lemmatizer.lemmatize(word, pos="n")  # Lemma as Noun
#     lemma_verb = lemmatizer.lemmatize(word, pos="v")  # Lemma as Verb
#     print("{0:20}{1:20}{2:20}".format(word, lemma_noun, lemma_verb))



#.............................................Lemmatization...................................

# from nltk.stem import WordNetLemmatizer


# lemmetaizer=WordNetLemmatizer()
# words=['eatting','eats','writing','writes','programing','programs','history','finally','finalized','ingeating']

# for word in words:
#     print(word+"------>"+lemmetaizer.lemmatize(word,pos='v'))
    
    
    
    
#............................................Paragraph........................................

sentence="""
The teachers were explaining different lessons to the students in the classrooms.
Some students were running quickly to finish their assignments on time.
Others were happily discussing new projects and preparing presentations.
A few children were writing stories and reading books in the library.
Finally, the principal was motivating everyone to keep working hard."""    

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmetization=WordNetLemmatizer()
words=word_tokenize(sentence)

print(words,type(words))

for lemma in words:
    print(lemma +"-------->"+lemmetization.lemmatize(lemma,pos='v'))
    

#.................................................................................................................................




#...............Stremming.......................

words=['eatting','eats','writing','writes','programing','programs','history','finally','finalized','ingeating']


#..................................posterStemmer...........................

from nltk.stem import PorterStemmer
stemming=PorterStemmer()

for word in words:
    print(word +"---->"+stemming.stem(word))


print(stemming.stem("Congratulation"))


#.......................................RegexpStemmer Class.................................
from nltk.stem import RegexpStemmer
re_stemmer=RegexpStemmer('ing|s$|e$|able$',min=4)

print(re_stemmer.stem('eating'))
print(re_stemmer.stem('eats'+"  "+'ingeating'+" "+'cars'+"  "+'mass'+" "+'computer'+" "+'adviseable'))


#........................................SnowBallStemmer..........................................

from nltk.stem import SnowballStemmer

snowballstremmer=SnowballStemmer('english')

for word in words:
    print(word,"---->",snowballstremmer.stem(word))
    
    #..................................................Difference............................
    

print(stemming.stem('fairly'+" "+'sportingly'+" "+'goes'))    
print(re_stemmer.stem('fairly'+" "+'sportingly'+" "+'goes'))    
print(snowballstremmer.stem('fairly'+" "+'sportingly'+" "+'goes'))    


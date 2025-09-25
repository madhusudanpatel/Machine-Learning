

sentence="The Eiffel Tower was built from 1887 to 1889 by French engineer Gustave Eiffel, whose company specialized in building metal frameworks and structures." """ Person Eg: Krish C Naik Place Or Location Eg: India Date Eg: September,24-09-1989 Time Eg: 4:30pm Money Eg: 1 million dollar Organization Eg: iNeuron Private Limited Percent Eg: 20%, twenty percent """

import nltk

words=nltk.word_tokenize(sentence)

tag_element=nltk.pos_tag(words)

# print(tag_element)


#....................................................................................................................

# nltk.download('maxent_ne_chunker')
# nltk.download('words')
#nltk.download('maxent_ne_chunker')

# chunked=nltk.ne_chunk(tag_element)
# print(chunked.draw())


# for subtree in chunked:
#     print(" ----Subtree----",subtree)
    

pronouns = [word for word, tag in tag_element if tag in ['NNP']]    
print("---NNP------:", pronouns)

pronouns1 = [word for word, tag in tag_element if tag in ['NN']]    
print("---NN----:", pronouns1)

pronouns2 = [word for word, tag in tag_element if tag in ['JJ']]    
print("----JJ----:", pronouns2)


from nltk.corpus import stopwords
stoplist =stopwords.words('english')
text=""" in computer ,stop words are words which are filtered out before ar after processeeing out  before or afte aproceessing of natural language data (text).
Though "stop words usually refers to the most common words in a language ,
there is no singale unvineral list of stop words used by al natural language processing tools, and inneed not all tools even use such a list.Some tools and indeed not all tool enven used such a list
Some tools specificallu avoid removine these stop words to support phrase seach .

""" 
print("\n Original Strint")
print(text)

clear_word_list=[word for word in text.split() if word not in stoplist]

print("\n After removing stop words from the said text:")
print(clear_word_list)
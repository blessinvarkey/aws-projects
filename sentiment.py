#TextBlob
#Sentiment analysis is the process of detecting positive, negative or neutral sentiment in a text.

from textblob import TextBlob, Word, WordList

#text = input('Write a statement \n')
text = 'There are many good day.'
words = TextBlob(text)
print(words[0:5])

#find(sub, start=0, end=9223372036854775807)
print(blob.replace(blob.words[4], blob.words[4].pluralize()))
word = Word("octopi")
lem = word.lemmatize()
print(lem)

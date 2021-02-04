#TextBlob
#Sentiment analysis is the process of detecting positive, negative or neutral sentiment in a text.

from textblob import TextBlob

#text = input('Write a statement \n')
text = 'There are many good day'

blob = TextBlob(text)


print(blob.replace(blob.words[4], blob.words[4].pluralize()))

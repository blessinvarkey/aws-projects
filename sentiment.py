from textblob import TextBlob


text = input('How was your day? \n')

blob = TextBlob(text)

polarity = blob.sentiment.polarity

if polarity <=0:
    print('This statement is negative')
else:
    print('This statement is positive')

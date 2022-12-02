import os 
os.system(pip install transformers)

from transformers import pipeline

def sentiment(tweet):
    classifier = pipeline('sentiment-analysis')
    return classifier(tweet)[0]['label']
tweet = " " #put your tweet -----> POSITIVE/ NEGATIVE
sentiment(tweet)

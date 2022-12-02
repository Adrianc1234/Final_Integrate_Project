from transformers import pipeline

def sentiment(tweet):
    classifier = pipeline('sentiment-analysis')
    return classifier(tweet)[0]['label']


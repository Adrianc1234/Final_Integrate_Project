import pandas as pd
import numpy as np
import string
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import re
import multiprocessing
import tensorflow as tf
from sklearn.model_selection import train_test_split
nltk.download("stopwords")

import warnings
warnings.filterwarnings("ignore")

from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
import re

#libraries for cleanning
from collections import Counter
pd.options.mode.chained_assignment = None
from collections import defaultdict
from string import punctuation 

# load model
from tensorflow.keras.models import load_model

def prediction(tweet):
    def scrub_words(text):
        # remove html markup
        text=re.sub("(<.*?>)","",text)
        
        #remove non-ascii and digits
        text=re.sub("(\\W|\\d)"," ",text)
    
        #remove whitespace
        text=text.strip()
        return text

    #Noise removal, stop word removal, normalizing?
    def cleanString(s, special_chars = "\":,.@|ðÿœžðÿâœœïÿœžÿºÿÿœžÿ"):
        for char in special_chars:
            s = s.replace(char, "")
        s = s.replace("\n", "")
        s = scrub_words(s)
        tokenizer = TweetTokenizer()
        stop_words = set(stopwords.words('english'))
        cleaned_words = [w for w in tokenizer.tokenize(s) if w not in 
stop_words]
        return " ".join(cleaned_words)

    def stemWords(sentence):
        stemmer, tokenizer = PorterStemmer(), TweetTokenizer()
        stemmed_words = [stemmer.stem(w) for w in 
tokenizer.tokenize(sentence)]
        return " ".join(stemmed_words)
        
    def cleanFrame(x):
        x = x.apply(cleanString)
        return x
    def stemFrame(x):
        x = x.apply(stemWords)
        return x


    savedModel=load_model('Model.h5')
    #savedModel.summary()
    x = pd.Series([tweet])
    x = cleanFrame(x)
    #print(x)
    x = stemFrame(x)
    #print(x)
    max_features = 20000
    # cut texts after this number of words
    # (among top max_features most common words)
    maxlen = 100
    batch_size = 32

    from keras.preprocessing import text
    # ✅ correct import
    from keras_preprocessing.sequence import pad_sequences

    tokenizer = text.Tokenizer(num_words=max_features)
    tokenizer.fit_on_texts(list(x))
    list_tokenized_train = tokenizer.texts_to_sequences(x)
    x = pad_sequences(list_tokenized_train, maxlen=maxlen)
    return savedModel.predict(x)[0][0]

#lets give a tweet
prediction("i want an Spotify account just so i can do the thing next year 
tbh")

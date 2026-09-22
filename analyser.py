from textblob import TextBlob
from transformers import pipeline
import requests
import random

emotion = pipeline("text-classification",model = "j-hartmann/emotion-english-distilroberta-base",top_k=1)

def get_qoute():
    try:
        datas = requests.get("https://zenquotes.io/api/quotes") # API
        data = datas.json()
        qoute = random.choice(data)
        return{
            "text" : qoute ["q"],
            "author" : qoute["a"]
        }
    except Exception as e:
        return{
            "text": "There is always light beyond darkness",
            "author": "Unknown"
        }


def get_sentiment(polarity):
    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

def analyse(text):
    blob = TextBlob(text)
    emotions = emotion(text)
    sentiment = get_sentiment(blob.sentiment.polarity)
    # extract  emotions
    emotions_label = emotions[0][0]["label"]
    emotions_score = emotions[0][0]["score"]
    quotes = get_qoute()
    result = { "sentiment" : sentiment,"emotions" : emotions_label, "score": round(emotions_score,2),"quotes":quotes}
    return result


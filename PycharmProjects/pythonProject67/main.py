from textblob import TextBlob
from flask_cors import CORS
from flask import Flask, request, jsonify


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello World"

class Emotion:
    sentiment: str
    score: float

    def __init__(self, sentiment: str, score: float):
        self.sentiment = sentiment
        self.score = score

def get_emotion(input_text: str, *, threshold: float) -> Emotion:
    sentiment: float = TextBlob(input_text).sentiment.polarity

    if sentiment >= threshold:
        return Emotion("Positive", sentiment)
    elif sentiment < 0.0:
        return Emotion("Negative", sentiment)
    else:
        return Emotion("Neutral", sentiment)


if __name__ == '__main__':
    while True:
        text = input('Text: ')
        emotion = get_emotion(text, threshold= 0.3)
        print(f'{emotion.sentiment}, {emotion.score}')






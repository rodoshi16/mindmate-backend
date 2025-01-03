from textblob import TextBlob
from flask_cors import CORS
from flask import Flask, request, jsonify
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

model_name = 'facebook/blenderbot-400M-distill'
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)

app = Flask(__name__)
CORS(app)

THRESHOLD = 0.3


def generate_response(input_text: str, chat_history: []):
    sentiment = TextBlob(input_text).sentiment.polarity

    if sentiment >= THRESHOLD:
        tone = ("The user is feeling positive. Keep the tone and the "
                "conversations positive and be "
                "enthusiastic and engaging")
    elif sentiment < 0.0:
        tone = ("The user is feeling upset. Ask them what happened and respond "
                "appropriately. If they are upset, show reassurance and "
                "give them comfort. If they are angry tell them you are there "
                "to listen.")
    else:
        tone = ("The user is feeling neutral. Ask them if they would like to "
                "talk about something or ask further questions about the topic "
                "you are discussing")

    prompt = (f"You are a Mental Health Assistant bot, your job is to listen to "
              f"your users and provide support. Talk to me like  "
              f"I am the user. Reply to the text of your user {input_text}, the "
              f"tone of your message should be {tone}, here's the history of the conversation "
              f"between you and the user {chat_history}")

    inputs = tokenizer([input_text], return_tensors='pt')
    reply_ids = model.generate(**inputs)
    response = tokenizer.batch_decode(reply_ids)
    return response


if __name__== '__main__':
    print(generate_response("What is my name", []))




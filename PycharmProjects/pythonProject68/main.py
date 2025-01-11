from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from textblob import TextBlob

app = Flask(__name__)
CORS(app, resources={r"/mindmate": {"origins": "http://localhost:3000"}})

THRESHOLD = 0.3


def find_sentiment(input_text: str):
    analyzed_text = TextBlob(input_text)
    return analyzed_text.sentiment.polarity


def generate_response(input_text: str, chat_history: []):
    sentiment = find_sentiment(input_text)

    if sentiment > THRESHOLD:
        tone = "respond with an uplifting tone."
    elif sentiment < -THRESHOLD:
        tone = "respond with empathy and support."
    else:
        tone = "respond in a helpful and understanding tone."

    prompt = (f"You are a mental health assistant bot. Here is the user's "
              f"message: '{input_text}'. {tone} Here is the "
              f"previous conversation: {chat_history}")

    model_input = tokenizer([input_text], return_tensors='pt')
    model_output = model.generate(**model_input)
    response = tokenizer.batch_decode(model_output, skip_special_tokens=True)[0]
    return response


@app.route('/mindmate', methods=['POST'])
def mindmate():
    data = request.json
    user_input = data.get('user_Input', '')
    chat_history = data.get('chat_history', [])

    response = generate_response(user_input, chat_history)
    chat_history.append({"sender": "Bot", "message": response})

    return jsonify({'response': response})


if __name__ == '__main__':
    model_name = "facebook/blenderbot-400M-distill"
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    app.run(debug=True)

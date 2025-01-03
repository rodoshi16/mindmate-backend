from textblob import TextBlob
from flask_cors import CORS
from flask import Flask, request, jsonify
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

app = Flask(__name__)
CORS(app, resources={r"/mindmate": {"origins": "http://localhost:5000"}})

THRESHOLD = 0.3


def is_hateful(input_text: str) -> bool:
    hateful_speech = ["murder", "kill", "suicide", "harm", "violence", "attack"]
    for word in input_text.split():
        if word in hateful_speech:
            return True
    return False


def generate_response(input_text: str, chat_history: []):
    sentiment = TextBlob(input_text).sentiment.polarity

    if is_hateful(input_text):
        tone = ("Do not provide advice or information about harmful, violent, "
                "respond "
                "with care and compassion and ask about what happened ")
    elif sentiment >= THRESHOLD:
        tone = "Positive and engaging"
    elif sentiment < 0.0:
        tone = "empathetic and comforting"
    else:
        tone = "neutral and supportive, encourage open ended conversations"

    prompt = (f"You are a mental health assistant bot. Your job is to listen, "
              f"understand, and respond appropriately based on user emotions. "
              f"Here is the user's latest message: '{input_text}'. The tone "
              f"of your response should be {tone}. Here is the previous "
              f"conversation history: {chat_history}")

    inputs = tokenizer([input_text], return_tensors='pt')
    reply_ids = model.generate(**inputs)
    response = tokenizer.batch_decode(reply_ids)
    return response

# Making an API endpoint
# mindmate is now a URL path the backend would listen to for HTTP requests


@app.route('/mindmate', methods=['GET', 'POST'])
def mindmate():
    # method to get the JSON data from the react frontend
    # frontend will make POST request to backend and send JSON data
    data = request.get_json()
    user_input = data.get('user_input')
    chat_history = data.get('chat_history', [])

    response = generate_response(user_input, chat_history)
    chat_history.append(f"User {user_input} Bot: {response}")
    return jsonify({'response': response})


if __name__ == '__main__':
    # if you put this outside the main block, it will error
    model_name = "facebook/blenderbot-400M-distill"
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    app.run(debug=True)


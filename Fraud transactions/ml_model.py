import pickle 
from dataset.py import model 
from flask import Flask, request, jsonify


with open('model.pkl', 'rb') as model_file: 
    model = pickle.load(model_file)


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    transaction_data = data['transaction']
    prediction = model.predict(['transaction_data'])

    if prediction[0] == 1:
        return jsonify({"fraud prediction": "fraud"})
    else:
        return jsnoify({"fraud prediction": "not fraud"})

if __name__ == '__main__':
    app.run(debug=True)




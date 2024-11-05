from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the model prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the request has JSON data
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    
    data = request.json
    
    # Check if 'features' is in the request data
    if 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400
    
    # Ensure features is a list
    features = data['features']
    if not isinstance(features, list):
        return jsonify({'error': 'Features must be a list'}), 400
    
    try:
        prediction = model.predict([features])
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
   

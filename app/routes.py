from flask import render_template, request, jsonify
from app import app
from app.ai import predict_wait_time

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('data')
    prediction = predict_wait_time(data)
    return jsonify({'prediction': prediction})

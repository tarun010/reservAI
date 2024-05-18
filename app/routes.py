from flask import render_template, request, jsonify, current_app as app
from .ai import predict_wait_time
from app.ai import predict_wait_time

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('data')
    prediction = predict_wait_time(data)
    return jsonify({'prediction': prediction})

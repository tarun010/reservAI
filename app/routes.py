from flask import render_template, request, jsonify, current_app as app
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from .ai import predict_wait_time

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = f"data/{filename}"
        file.save(file_path)
        
        # Process the CSV file and make predictions
        df = pd.read_csv(file_path)
        predictions = []
        for index, row in df.iterrows():
            pred = predict_wait_time(row['num_patients'], row['time_of_day'], row['day_of_week'])
            predictions.append({
                'num_patients': int(row['num_patients']),
                'time_of_day': int(row['time_of_day']),
                'day_of_week': int(row['day_of_week']),
                'predicted_wait_time': float(pred)  # Convert to standard Python float
            })
        return jsonify(predictions)
    return jsonify({'error': 'File type not allowed'}), 400

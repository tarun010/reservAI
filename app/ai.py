import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def load_and_preprocess_data(file_path):
    # Load the dummy dataset
    df = pd.read_csv(file_path)
    
    # Convert columns to appropriate data types
    df['num_patients'] = df['num_patients'].astype(int)
    df['time_of_day'] = df['time_of_day'].astype(int)
    df['day_of_week'] = df['day_of_week'].astype(int)
    df['wait_time'] = df['wait_time'].astype(float)
    
    return df

def train_model(df):
    # Features and target variable
    X = df[['num_patients', 'time_of_day', 'day_of_week']]
    y = df['wait_time']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Model trained. Mean Squared Error: {mse}')

    return model

# Load and preprocess data
file_path = 'data/dummy_data.csv'
df = load_and_preprocess_data(file_path)

# Train the model
model = train_model(df)

def predict_wait_time(num_patients, time_of_day, day_of_week):
    # Ensure inputs are in the correct format
    X_new = np.array([[num_patients, time_of_day, day_of_week]])
    prediction = model.predict(X_new)
    return prediction[0]

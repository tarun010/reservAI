import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Example: Function to prepare data
def prepare_data():
    # Dummy data: Replace with actual historical data
    data = {
        'num_people': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'time_of_day': [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],  # e.g., 9 AM to 6 PM
        'day_of_week': [1, 2, 3, 4, 5, 6, 7, 1, 2, 3],  # e.g., Monday to Sunday
        'wait_time': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]  # Dummy wait times
    }
    df = pd.DataFrame(data)
    
    # Features and target variable
    X = df[['num_people', 'time_of_day', 'day_of_week']]
    y = df['wait_time']
    
    return X, y

# Function to train the model
def train_model():
    X, y = prepare_data()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model trained. Mean Squared Error: {mse}")
    
    return model

# Train the model and save it globally
model = train_model()

# Function to predict wait time
def predict_wait_time(num_people, time_of_day, day_of_week):
    prediction = model.predict(np.array([[num_people, time_of_day, day_of_week]]))
    return prediction[0]

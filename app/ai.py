import numpy as np
from sklearn.linear_model import LinearRegression

def predict_wait_time(data):
    # Dummy example for predictive model
    model = LinearRegression()
    model.fit(np.array([[1], [2], [3]]), np.array([1, 2, 3]))
    prediction = model.predict(np.array([[data]]))
    return prediction[0]

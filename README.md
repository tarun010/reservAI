# wAItless

wAItless is a wait list management system designed to reduce wait times at busy locations such as hospitals, restaurants, museums, and labs. This application leverages AI to predict wait times, optimize resource allocation, and enhance user experience.


## Demo 1 - Input customer details, Predict Wait Time
[<img width="1191" alt="wAItless-demo" src="https://github.com/tarun010/reservAI/assets/25506296/1caaf7c1-39d6-4c50-b089-3b067a2c408d">](https://youtu.be/lq9U7crYBlc?si=kOqMGutwTaXAOlAy)

## Demo 2 - Get customer data from Client, Predict Wait Time
[<img width="1191" alt="Screenshot 2024-05-19 at 14 06 50" src="https://github.com/tarun010/reservAI/assets/25506296/3f7e5c01-dc9c-43ca-abb0-95cdef6f9846">](https://youtu.be/7SjWcDdM9F0?si=l2ojn8HvJgg9x4G1)


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Predictive wait time estimation using machine learning
- User-friendly interface with responsive design
- Real-time waitlist updates
- Chatbot assistance for user queries
- Resource optimization based on user behavior analysis

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/tarun010/reservAI
    cd reservAI
    ```

2. **Create and activate a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. **Run the application**
    ```bash
    flask run
    ```

## Usage

- Open your browser and go to `http://127.0.0.1:5000` to see the application in action.
- Use the navigation bar to explore different features.
- Use the chatbot for assistance and inquiries about wait times.

## Project Structure
reservAI/ \
│ \
├── app/ \
│   ├── __init__.py \
│   ├── templates/ \
│   │   └── index.html \
│   ├── static/ \
│   │   ├── css/ \
│   │   │   └── style.css \
│   ├── routes.py \
│   ├── models.py \
│   └── ai.py \
│ \
├── venv/ \
├── config.py \
├── requirements.txt \
└── run.py \



## Technologies
- Frontend: Flask with Jinja2 templating, Bootstrap for styling
- Backend: Flask, SQLAlchemy for ORM
- AI/ML: TensorFlow, scikit-learn
## Features
- Predictive Wait Time Estimation: Uses machine learning to predict wait times based on historical data.
- User Interaction: Allows users to join the waitlist, view current wait times, and receive notifications.
- Resource Optimization: Optimizes resource allocation based on predicted demand.

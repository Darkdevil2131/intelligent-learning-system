# intelligence.py

import json
import os
import numpy as np
from sklearn.linear_model import LogisticRegression

FILE = "performance.json"


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

def load_data():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []


# --------------------------------------------------
# PREPARE DATASET
# --------------------------------------------------

def prepare_dataset(data):
    """
    Convert performance history into ML dataset
    """

    if len(data) < 5:
        return None, None

    X = []
    y = []

    for i in range(1, len(data)):
        prev_score = data[i - 1]["score"]
        current_score = data[i]["score"]

        # Feature: previous score
        X.append([prev_score])

        # Label: good (>=7) or bad
        y.append(1 if current_score >= 7 else 0)

    return np.array(X), np.array(y)


# --------------------------------------------------
# TRAIN MODEL
# --------------------------------------------------

def train_model():
    data = load_data()

    X, y = prepare_dataset(data)

    if X is None:
        return None

    model = LogisticRegression()
    model.fit(X, y)

    return model


# --------------------------------------------------
# PREDICT PERFORMANCE
# --------------------------------------------------

def predict_performance(last_score):
    model = train_model()

    if model is None:
        return "Not enough data to learn yet."

    prediction = model.predict([[last_score]])[0]

    if prediction == 1:
        return "You are likely to perform well next."
    else:
        return "You may struggle next. Focus on basics."


# --------------------------------------------------
# TREND ANALYSIS
# --------------------------------------------------

def analyze_trend():
    data = load_data()

    if len(data) < 3:
        return "Not enough data to detect trend."

    scores = [d["score"] for d in data]

    if scores[-1] > scores[-2] > scores[-3]:
        return "You are improving consistently 📈"

    elif scores[-1] < scores[-2] < scores[-3]:
        return "Performance is declining 📉"

    else:
        return "Performance is fluctuating ⚖️"
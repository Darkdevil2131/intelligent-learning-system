import json
import os
import numpy as np
from sklearn.linear_model import SGDClassifier

FILE = "performance.json"


class AdaptiveModel:

    def __init__(self):
        self.model = SGDClassifier(loss="log_loss")
        self.initialized = False

    # --------------------------------------------------
    # LOAD DATA
    # --------------------------------------------------

    def load_data(self):
        if not os.path.exists(FILE):
            return []

        with open(FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return []

    # --------------------------------------------------
    # PREPARE STREAM DATA
    # --------------------------------------------------

    def prepare_data(self, data):

        if len(data) < 2:
            return None, None

        X = []
        y = []

        for i in range(1, len(data)):
            prev = data[i - 1]["score"]
            curr = data[i]["score"]

            X.append([prev])
            y.append(1 if curr >= 7 else 0)

        return np.array(X), np.array(y)

    # --------------------------------------------------
    # ONLINE TRAINING
    # --------------------------------------------------

    def train(self):

        data = self.load_data()
        X, y = self.prepare_data(data)

        if X is None:
            return False

        if not self.initialized:
            self.model.partial_fit(X, y, classes=np.array([0, 1]))
            self.initialized = True
        else:
            self.model.partial_fit(X, y)

        return True

    # --------------------------------------------------
    # PREDICT NEXT BEHAVIOR
    # --------------------------------------------------

    def predict(self, last_score):

        if not self.initialized:
            return "Model not trained yet."

        pred = self.model.predict([[last_score]])[0]

        if pred == 1:
            return "📈 You are improving dynamically"
        else:
            return "📉 Performance may decline — adjust strategy"
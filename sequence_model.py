import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


class SequenceModel:

    def __init__(self):
        self.model = Sequential([
            LSTM(32, input_shape=(3, 1)),
            Dense(1, activation='sigmoid')
        ])

        self.model.compile(optimizer='adam', loss='binary_crossentropy')

    def prepare_data(self, scores):
        X, y = [], []

        for i in range(3, len(scores)):
            X.append(scores[i-3:i])
            y.append(1 if scores[i] >= 10 else 0)

        X = np.array(X).reshape(-1, 3, 1)
        y = np.array(y)

        return X, y

    def train(self, scores):
        if len(scores) < 5:
            return

        X, y = self.prepare_data(scores)
        self.model.fit(X, y, epochs=10, verbose=0)

    def predict(self, scores):
        if len(scores) < 3:
            return 0.5

        last = np.array(scores[-3:]).reshape(1, 3, 1)
        return float(self.model.predict(last, verbose=0)[0][0])
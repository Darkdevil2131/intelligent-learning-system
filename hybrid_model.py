from real_model import RealModel
from sequence_model import SequenceModel


class HybridModel:

    def __init__(self):
        self.real = RealModel()
        self.seq = SequenceModel()

    def train(self):
        score = self.real.train()
        return score

    def predict(self, studytime, failures, absences, G1, G2, history):

        # ML prediction
        rf_pred = self.real.predict(studytime, failures, absences, G1, G2)

        # LSTM behavior prediction
        self.seq.train(history)
        lstm_pred = self.seq.predict(history)

        # 🔥 HYBRID COMBINATION
        final = (rf_pred * 0.8) + (lstm_pred * 20 * 0.2)

        return {
            "rf": rf_pred,
            "lstm": lstm_pred,
            "final": final
        }
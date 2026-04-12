import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


class RealModel:

    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.features = ['studytime', 'failures', 'absences', 'G1', 'G2']
        self.target = 'G3'

    def load_data(self):
        # Load dataset with correct separator
        df = pd.read_csv("student-mat.csv", sep=';')

        # 🔥 CLEAN COLUMN NAMES (handles your broken file)
        df.columns = df.columns.astype(str)
        df.columns = df.columns.str.replace('"', '', regex=False)
        df.columns = df.columns.str.replace('[', '', regex=False)
        df.columns = df.columns.str.replace(']', '', regex=False)
        df.columns = df.columns.str.strip()

        # Debug print (you can remove later)
        print("Columns:", df.columns.tolist())

        return df

    def preprocess(self, df):
        # Ensure required columns exist
        missing = [col for col in self.features + [self.target] if col not in df.columns]

        if missing:
            raise Exception(f"Missing columns: {missing}")

        X = df[self.features]
        y = df[self.target]

        return X, y

    def train(self):
        df = self.load_data()
        X, y = self.preprocess(df)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        self.model.fit(X_train, y_train)

        score = self.model.score(X_test, y_test)
        return score

    def predict(self, studytime, failures, absences, G1, G2):
        data = pd.DataFrame(
            [[studytime, failures, absences, G1, G2]],
            columns=self.features
        )

        prediction = self.model.predict(data)[0]
        return prediction
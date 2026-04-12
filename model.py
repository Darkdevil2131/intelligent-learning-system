"""
model.py

Core ML pipeline:
- Load data
- Preprocess
- Train multiple models
- Evaluate properly
- Select best model
- Provide explainability
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


# --------------------------------------------------
# DATA LOADING
# --------------------------------------------------

def load_data(file_path: str) -> pd.DataFrame:
    """Load dataset from CSV file"""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise RuntimeError(f"Error loading data: {e}")


# --------------------------------------------------
# PREPROCESSING
# --------------------------------------------------

def preprocess_data(data: pd.DataFrame):
    """
    Prepare data for ML:
    - Encode target variable
    - Split features and labels
    """

    df = data.copy()

    # Encode target (Pass/Fail → 1/0)
    encoder = LabelEncoder()
    df["Result"] = encoder.fit_transform(df["Result"])

    # Features and target
    X = df.drop(columns=["Name", "Result"])
    y = df["Result"]

    return X, y, encoder


# --------------------------------------------------
# MODEL TRAINING + SELECTION
# --------------------------------------------------

def train_and_select_model(X, y):
    """
    Train multiple models and select the best one
    based on accuracy (can extend later)
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y  # better distribution
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    best_model = None
    best_score = 0.0
    best_name = ""

    print("\n========== MODEL EVALUATION ==========")

    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        print(f"\n{name}")
        print("-" * len(name))
        print(f"Accuracy: {accuracy:.2f}")

        print("\nConfusion Matrix:")
        print(confusion_matrix(y_test, predictions))

        print("\nClassification Report:")
        print(classification_report(y_test, predictions))

        # Select best model
        if accuracy > best_score:
            best_score = accuracy
            best_model = model
            best_name = name

    return best_model, best_name, X_test, y_test


# --------------------------------------------------
# MODEL EXPLAINABILITY
# --------------------------------------------------

def explain_model(model, feature_names):
    """
    Show feature importance if supported
    """

    print("\n========== MODEL EXPLANATION ==========")

    if hasattr(model, "feature_importances_"):
        importance = model.feature_importances_

        feature_importance = sorted(
            zip(feature_names, importance),
            key=lambda x: x[1],
            reverse=True
        )

        print("Feature Importance (sorted):")
        for feature, score in feature_importance:
            print(f"{feature:<12} → {score:.3f}")

    else:
        print("This model does not support feature importance.")


# --------------------------------------------------
# PREDICTION FUNCTION (IMPORTANT UPGRADE)
# --------------------------------------------------

def predict_new_student(model, encoder, input_data: dict):
    """
    Predict Pass/Fail for a new student

    input_data example:
    {
        "Math": 50,
        "Science": 60,
        "English": 55,
        "Attendance": 70
    }
    """

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]
    result = encoder.inverse_transform([prediction])[0]

    return result
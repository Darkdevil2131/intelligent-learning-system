# tracker.py

import json
import os

FILE_NAME = "performance.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def add_record(module, score):
    data = load_data()
    data.append({
        "module": module,
        "score": score
    })
    save_data(data)


def show_progress():
    data = load_data()

    if not data:
        print("No performance data available.")
        return

    print("\n========== PERFORMANCE HISTORY ==========\n")

    for i, record in enumerate(data, 1):
        print(f"{i}. {record['module']} → Score: {record['score']}")

    avg = sum(item["score"] for item in data) / len(data)
    print(f"\nAverage Score: {round(avg, 2)}")
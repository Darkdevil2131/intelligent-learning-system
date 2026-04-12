# pattern_analyzer.py

import json
import os

FILE = "patterns.json"


def load_patterns():
    if not os.path.exists(FILE):
        data = {"logic_errors": 0, "syntax_errors": 0}
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return data

    with open(FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            data = {"logic_errors": 0, "syntax_errors": 0}
            with open(FILE, "w", encoding="utf-8") as wf:
                json.dump(data, wf, indent=4)
            return data


def save_patterns(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def update_patterns(results):
    data = load_patterns()

    for result in results:
        if not result["passed"]:
            if "error" in result:
                data["syntax_errors"] += 1
            else:
                data["logic_errors"] += 1

    save_patterns(data)


def show_patterns():
    data = load_patterns()

    print("\n========== ERROR PATTERNS ==========")
    print(f"Syntax Errors: {data['syntax_errors']}")
    print(f"Logic Errors: {data['logic_errors']}")

    if data["logic_errors"] > data["syntax_errors"]:
        print("You struggle more with logic.")
    else:
        print("You struggle more with syntax.")
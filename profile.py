# profile.py

def generate_profile(data):
    if not data:
        print("No data available.")
        return

    avg = sum(d["score"] for d in data) / len(data)

    print("\n========== LEARNING PROFILE ==========")

    print(f"Average Score: {round(avg, 2)}")

    if avg >= 8:
        print("Level: Advanced Learner")
    elif avg >= 5:
        print("Level: Intermediate Learner")
    else:
        print("Level: Beginner")

    print("Advice: Stay consistent and practice regularly.")
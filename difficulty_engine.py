# difficulty_engine.py

def get_difficulty(score):

    if score >= 8:
        return "HARD"
    elif score >= 5:
        return "MEDIUM"
    else:
        return "EASY"


def next_action(score):

    if score >= 8:
        return "Increase difficulty + introduce complex problems"
    elif score >= 5:
        return "Keep medium level + practice more"
    else:
        return "Go back to basics + guided learning"
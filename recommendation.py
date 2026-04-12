# recommendation.py

def suggest_improvement(score, module):
    if score >= 8:
        return f"Great performance in {module}. Try advanced problems."

    elif score >= 5:
        return f"You are doing okay in {module}. Practice more medium-level problems."

    else:
        return f"You are weak in {module}. Focus on basics and revise concepts."
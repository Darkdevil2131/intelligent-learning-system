

import re


# --------------------------------------------------
# BASIC MATH PROBLEMS (CAN EXPAND LATER)
# --------------------------------------------------

def get_problem():
    return {
        "question": "Solve: 2x + 3 = 7",
        "answer": 2
    }


# --------------------------------------------------
# ANSWER PARSER
# --------------------------------------------------

def extract_number(answer):
    """
    Extract numeric value from student input
    """
    numbers = re.findall(r'-?\d+', answer)

    if numbers:
        return int(numbers[-1])

    return None


# --------------------------------------------------
# EVALUATION ENGINE
# --------------------------------------------------

def evaluate_math_answer(student_answer, correct_answer):
    """
    Compare student answer with correct answer
    """

    student_value = extract_number(student_answer)

    if student_value is None:
        return {
            "correct": False,
            "message": "Could not understand your answer."
        }

    if student_value == correct_answer:
        return {
            "correct": True,
            "message": "Correct solution."
        }

    return {
        "correct": False,
        "message": f"Incorrect. Expected {correct_answer}, got {student_value}."
    }


# --------------------------------------------------
# SCORING
# --------------------------------------------------

def calculate_score(is_correct):
    return 10 if is_correct else 3


# --------------------------------------------------
# FEEDBACK SYSTEM
# --------------------------------------------------

def generate_feedback(is_correct):
    if is_correct:
        return "Good job. Your mathematical reasoning seems correct."

    return (
        "Review your steps carefully.\n"
        "Suggestion: Isolate variable step-by-step and re-check calculations."
    )
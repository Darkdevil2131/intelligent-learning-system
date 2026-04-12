# main.py

from model import (
    load_data,
    preprocess_data,
    train_and_select_model,
    explain_model
)

from coding_engine import (
    run_code,
    calculate_score,
    generate_feedback,
    format_results,
    get_performance_level
)

from math_engine import (
    get_problem,
    evaluate_math_answer,
    calculate_score as math_score,
    generate_feedback as math_feedback
)

from tracker import add_record, show_progress, load_data as load_perf_data
from recommendation import suggest_improvement
from pattern_analyzer import update_patterns, show_patterns
from profile import generate_profile


# --------------------------------------------------
# ML ANALYSIS SYSTEM
# --------------------------------------------------

def run_ml_system():
    print("\n========== ML ANALYSIS ==========\n")

    try:
        data = load_data("data.csv")
        X, y, encoder = preprocess_data(data)
        model, model_name, X_test, y_test = train_and_select_model(X, y)

        print(f"\nBest Model Selected: {model_name}")
        explain_model(model, X.columns)

    except Exception as e:
        print("Error in ML system:", e)


# --------------------------------------------------
# CODING EVALUATION SYSTEM
# --------------------------------------------------

def run_coding_evaluation():
    print("\n========== CODING EVALUATION ==========\n")

    print("Problem: Add two numbers\n")

    print("Write your function (must be named 'solution')")
    print("Example:")
    print("def solution(a, b):")
    print("    return a + b\n")

    user_code = ""
    print("Enter your code (type 'END' on a new line to finish):")

    while True:
        line = input()
        if line.strip() == "END":
            break
        user_code += line + "\n"

    test_cases = [
        ((2, 3), 5),
        ((5, 7), 12),
        ((0, 0), 0),
        ((-1, 1), 0),
        ((100, 200), 300)
    ]

    try:
        results = run_code(user_code, test_cases)

        score = calculate_score(results)
        feedback = generate_feedback(results)
        formatted_results = format_results(results)
        performance = get_performance_level(score)

        print("\n---------- TEST RESULTS ----------")
        for line in formatted_results:
            print(line)

        print("\n---------- FINAL RESULT ----------")
        print(f"Score: {score}/10")
        print(f"Performance Level: {performance}")
        print("Feedback:")
        print(feedback)

        # Save performance
        add_record("Coding", score)

        # Update pattern tracking
        update_patterns(results)

        # Recommendation
        suggestion = suggest_improvement(score, "Coding")
        print("\nRecommendation:")
        print(suggestion)

        # Adaptive difficulty
        if score >= 8:
            difficulty = "Hard"
        elif score >= 5:
            difficulty = "Medium"
        else:
            difficulty = "Easy"

        print(f"Next Problem Difficulty: {difficulty}")

    except Exception as e:
        print("Error during evaluation:", e)


# --------------------------------------------------
# MATH EVALUATION SYSTEM
# --------------------------------------------------

def run_math_evaluation():
    print("\n========== MATH EVALUATION ==========\n")

    problem = get_problem()

    print("Question:", problem["question"])

    student_answer = input("Enter your answer: ")

    result = evaluate_math_answer(student_answer, problem["answer"])

    score = math_score(result["correct"])
    feedback = math_feedback(result["correct"])

    print("\n---------- RESULT ----------")
    print(result["message"])
    print(f"Score: {score}/10")
    print("Feedback:")
    print(feedback)

    # Save performance
    add_record("Math", score)

    # Recommendation
    suggestion = suggest_improvement(score, "Math")
    print("\nRecommendation:")
    print(suggestion)


# --------------------------------------------------
# MAIN MENU SYSTEM
# --------------------------------------------------

def main():
    print("🎯 Intelligent Learning System\n")

    while True:
        print("\nChoose an option:")
        print("1. Run ML Analysis")
        print("2. Run Coding Evaluation")
        print("3. Run Math Evaluation")
        print("4. View Performance")
        print("5. View Error Patterns")
        print("6. View Learning Profile")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            run_ml_system()

        elif choice == "2":
            run_coding_evaluation()

        elif choice == "3":
            run_math_evaluation()

        elif choice == "4":
            show_progress()

        elif choice == "5":
            show_patterns()

        elif choice == "6":
            data = load_perf_data()
            generate_profile(data)

        elif choice == "7":
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Please try again.")


# --------------------------------------------------

if __name__ == "__main__":
    main()
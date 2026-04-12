# coding_engine.py

import traceback


# --------------------------------------------------
# CODE EXECUTION ENGINE
# --------------------------------------------------

def run_code(user_code, test_cases):
    """
    Executes user code and evaluates against test cases.
    """

    results = []

    for i, (inputs, expected_output) in enumerate(test_cases):
        try:
            local_env = {}

            # Execute user code
            exec(user_code, {}, local_env)

            if "solution" not in local_env:
                raise Exception("Function 'solution' not defined")

            result = local_env["solution"](*inputs)

            passed = result == expected_output

            results.append({
                "test_case": i + 1,
                "input": inputs,
                "expected": expected_output,
                "got": result,
                "passed": passed
            })

        except Exception:
            results.append({
                "test_case": i + 1,
                "error": traceback.format_exc(),
                "passed": False
            })

    return results


# --------------------------------------------------
# SCORING SYSTEM
# --------------------------------------------------

def calculate_score(results):
    """
    Returns score out of 10.
    """

    total = len(results)
    passed = sum(1 for r in results if r["passed"])

    return round((passed / total) * 10, 2)


# --------------------------------------------------
# PERFORMANCE LEVEL CLASSIFICATION
# --------------------------------------------------

def get_performance_level(score):
    """
    Classify performance level based on score.
    """

    if score == 10:
        return "Expert"
    elif score >= 7:
        return "Good"
    elif score >= 4:
        return "Beginner"
    else:
        return "Needs Improvement"


# --------------------------------------------------
# INTELLIGENT FEEDBACK SYSTEM
# --------------------------------------------------

def generate_feedback(results):
    """
    Analyze mistakes and generate meaningful feedback.
    """

    failed = [r for r in results if not r["passed"]]

    if not failed:
        return "All test cases passed. Excellent work."

    error_count = sum(1 for r in failed if "error" in r)
    wrong_output_count = len(failed) - error_count

    feedback = []
    suggestions = []

    # Error analysis
    if error_count > 0:
        feedback.append("Your code has syntax or runtime errors.")
        suggestions.append("Check indentation, syntax, and function definition.")

    # Logic issues
    if wrong_output_count > 0:
        feedback.append("Your logic is incorrect for some test cases.")
        suggestions.append("Re-evaluate your approach and dry-run your code.")

    # Edge case detection
    if wrong_output_count > 1:
        feedback.append("Your code may not handle edge cases properly.")
        suggestions.append("Test with edge values like 0, negatives, and large inputs.")

    # General improvement
    suggestions.append("Practice solving similar problems to improve logic.")

    return " ".join(feedback) + "\nSuggestions: " + " ".join(suggestions)


# --------------------------------------------------
# RESULT FORMATTER
# --------------------------------------------------

def format_results(results):
    """
    Converts raw results into readable output.
    """

    formatted = []

    for r in results:
        if r["passed"]:
            formatted.append(f"Test {r['test_case']}: ✅ Passed")
        else:
            if "error" in r:
                formatted.append(f"Test {r['test_case']}: ❌ Error")
            else:
                formatted.append(
                    f"Test {r['test_case']}: ❌ Failed (Expected {r['expected']}, Got {r['got']})"
                )

    return formatted
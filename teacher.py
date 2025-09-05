import pickle
from utils import slow_print, banner

QUESTIONS_FILE = "quest.bin"

def add_question():
    """Allows a teacher to add new questions to the question bank."""
    banner("Teacher Interface - Add Question")
    slow_print("Welcome, Teacher! Add your questions to the quiz.", 0.01)

    question = input("Enter the question: ").strip()
    option_a = input("Enter option a: ").strip()
    option_b = input("Enter option b: ").strip()
    option_c = input("Enter option c: ").strip()

    while True:
        correct = input("Enter the correct option [a/b/c]: ").lower()
        if correct in ("a", "b", "c"):
            break
        else:
            print("⚠️ Please choose only a, b, or c.")

    # prepare structure
    q_data = {question: [option_a, option_b, option_c, correct]}

    # save to binary file
    with open(QUESTIONS_FILE, "ab") as f:
        pickle.dump(q_data, f)

    print("✅ Question added successfully!")

def view_questions():
    """Allows teacher to view all questions in the question bank."""
    banner("📚 Teacher Interface - Question Bank")
    try:
        with open(QUESTIONS_FILE, "rb") as f:
            i = 1
            while True:
                try:
                    data = pickle.load(f)
                    for q, opts in data.items():
                        print(f"\nQ{i}. {q}")
                        print(f"   a) {opts[0]}")
                        print(f"   b) {opts[1]}")
                        print(f"   c) {opts[2]}")
                        print(f"   ✅ Correct Answer: {opts[3]}")
                        print("-" * 50)
                        i += 1
                except EOFError:
                    break
    except FileNotFoundError:
        print("⚠️ No questions found. Please add some first.")

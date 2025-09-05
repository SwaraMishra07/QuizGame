import pickle
from utils import slow_print, banner

QUESTIONS_FILE = "quest.bin"

def start_exam():
    """Runs the student exam loop."""
    banner("Student Exam Interface")

    slow_print("📢 Exam is starting! Please answer carefully.", 0.02)
    slow_print("Rules:", 0.02)
    print("✔️  Correct Answer = +4 points")
    print("❌  Wrong Answer   = -1 point")
    print("➡️  Skip (option d) = 0 points")
    print("-" * 50)

    name = input("Enter your name: ").strip()
    correct = incorrect = skipped = score = 0
    q_number = 1

    try:
        with open(QUESTIONS_FILE, "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                    for q, opts in data.items():
                        print(f"\n{q_number}. {q}")
                        print(f"   a) {opts[0]}")
                        print(f"   b) {opts[1]}")
                        print(f"   c) {opts[2]}")
                        print("   d) Skip")

                        choice = input("Your answer [a/b/c/d]: ").lower().strip()

                        if choice == opts[3]:
                            print("✅ Correct!")
                            correct += 1
                            score += 4
                        elif choice == "d":
                            print("➡️ Skipped")
                            skipped += 1
                        elif choice in ("a", "b", "c"):
                            print("❌ Wrong!")
                            incorrect += 1
                            score -= 1
                        else:
                            print("⚠️ Invalid input! Question skipped.")
                            skipped += 1

                        q_number += 1
                except EOFError:
                    break
    except FileNotFoundError:
        print("⚠️ No questions available. Ask a teacher to add some first.")
        return None

    return {
        "name": name,
        "correct": correct,
        "incorrect": incorrect,
        "skipped": skipped,
        "score": score
    }


def show_result(result: dict):
    """Displays the student’s results."""
    banner("📊 Exam Results")
    if not result:
        print("No result to show.")
        return
    print(f"Student: {result['name']}")
    print(f"✔️ Correct:   {result['correct']}")
    print(f"❌ Incorrect: {result['incorrect']}")
    print(f"➡️ Skipped:   {result['skipped']}")
    print(f"🏆 Total Score: {result['score']}")
    print("=" * 50)

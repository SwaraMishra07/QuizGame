# app.py
import streamlit as st
import pickle
import csv
import os
import pandas as pd

QUESTIONS_FILE = "quest.bin"
RESULTS_FILE = "results.csv"

st.set_page_config(page_title="QuizMaster", page_icon="🎓", layout="centered")

# ---------------------- Teacher Functions ----------------------
def add_question(q, a, b, c, ans):
    data = {q: [a, b, c, ans]}
    with open(QUESTIONS_FILE, "ab") as f:
        pickle.dump(data, f)

def view_questions():
    if not os.path.exists(QUESTIONS_FILE):
        st.warning("⚠️ No questions found yet.")
        return

    i = 1
    with open(QUESTIONS_FILE, "rb") as f:
        while True:
            try:
                data = pickle.load(f)
                for q, opts in data.items():
                    st.write(f"**Q{i}. {q}**")
                    st.write(f"a) {opts[0]}")
                    st.write(f"b) {opts[1]}")
                    st.write(f"c) {opts[2]}")
                    st.success(f"✅ Correct Answer: {opts[3]}")
                    st.markdown("---")
                    i += 1
            except EOFError:
                break

# ---------------------- Student Functions ----------------------
def start_exam(name):
    if not os.path.exists(QUESTIONS_FILE):
        st.warning("⚠️ No questions available.")
        return None

    correct = incorrect = skipped = score = 0
    answers = []

    with open(QUESTIONS_FILE, "rb") as f:
        i = 1
        while True:
            try:
                data = pickle.load(f)
                for q, opts in data.items():
                    st.write(f"**Q{i}. {q}**")
                    choice = st.radio(
                        f"Your Answer for Q{i}",
                        ["a", "b", "c", "Skip"],
                        key=f"q{i}"
                    )
                    if choice.lower() == opts[3]:
                        correct += 1
                        score += 4
                        answers.append((q, "✅ Correct"))
                    elif choice == "Skip":
                        skipped += 1
                        answers.append((q, "➡️ Skipped"))
                    else:
                        incorrect += 1
                        score -= 1
                        answers.append((q, "❌ Wrong"))
                    i += 1
            except EOFError:
                break

    # Save results
    save_result(name, correct, incorrect, skipped, score)
    return {
        "name": name,
        "correct": correct,
        "incorrect": incorrect,
        "skipped": skipped,
        "score": score,
        "answers": answers
    }

# ---------------------- Results Handling ----------------------
def save_result(name, correct, incorrect, skipped, score):
    file_exists = os.path.exists(RESULTS_FILE)
    with open(RESULTS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Correct", "Incorrect", "Skipped", "Score"])
        writer.writerow([name, correct, incorrect, skipped, score])

def show_performance():
    if not os.path.exists(RESULTS_FILE):
        st.warning("⚠️ No results yet.")
        return
    df = pd.read_csv(RESULTS_FILE)
    df = df.sort_values("Score", ascending=False)
    st.dataframe(df, use_container_width=True)

# ---------------------- Streamlit App ----------------------
st.title("🎓 QuizMaster: Student–Teacher Quiz System")

menu = ["🏠 Home", "👨‍🏫 Teacher", "👩‍🎓 Student", "🏆 Performance Board"]
choice = st.sidebar.radio("Navigate", menu)

if choice == "🏠 Home":
    st.subheader("Welcome 👋")
    st.write("This is a fun **Quiz System** for Teachers & Students.")
    st.info("👉 Use the sidebar to navigate between Teacher, Student, and Performance Board.")

elif choice == "👨‍🏫 Teacher":
    st.subheader("👨‍🏫 Teacher Dashboard")

    with st.form("add_q_form"):
        q = st.text_input("Enter Question")
        a = st.text_input("Option A")
        b = st.text_input("Option B")
        c = st.text_input("Option C")
        ans = st.radio("Correct Answer", ["a", "b", "c"])
        submitted = st.form_submit_button("Add Question")

        if submitted and q and a and b and c:
            add_question(q, a, b, c, ans)
            st.success("✅ Question Added!")

    if st.button("📚 View Questions"):
        view_questions()

elif choice == "👩‍🎓 Student":
    st.subheader("👩‍🎓 Student Exam")

    name = st.text_input("Enter Your Name")
    if name and st.button("Start Exam"):
        result = start_exam(name)
        if result:
            st.success(f"🎉 Exam Completed! Score: {result['score']}")
            st.write("### 📊 Detailed Results")
            st.write(f"✔️ Correct: {result['correct']}")
            st.write(f"❌ Incorrect: {result['incorrect']}")
            st.write(f"➡️ Skipped: {result['skipped']}")
            st.markdown("---")
            for q, res in result["answers"]:
                st.write(f"**{q}** → {res}")

elif choice == "🏆 Performance Board":
    st.subheader("🏆 Leaderboard")
    show_performance()

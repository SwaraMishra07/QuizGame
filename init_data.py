import os
import csv
import pickle

# Dummy users
users = [
    ["teacher1", "teach123"],
    ["student1", "stud123"],
    ["student2", "stud456"],
    ["guest", "guest"]
]

# Funny questions
questions = {
    "What is Chemistry?": [
        "Study of matter",
        "A chemist's tree 🌳",
        "Stupid subject",
        "Study of matter"
    ],
    "Why did the computer go to therapy?": [
        "Because it caught a virus 💻🤒",
        "Because it lost its memory",
        "Because it was overheating",
        "Because it caught a virus 💻🤒"
    ],
    "Best way to pass exams?": [
        "Study hard 📚",
        "Make friends with the teacher 😏",
        "Ctrl + C, Ctrl + V",
        "Study hard 📚"
    ],
    "What is Python?": [
        "A programming language 🐍",
        "A giant snake that codes",
        "My nightmare before exams",
        "A programming language 🐍"
    ],
    "Why was the math book sad?": [
        "Too many problems 😢",
        "Because no one opened it",
        "It hated fractions",
        "Too many problems 😢"
    ]
}

# Create user.csv
if not os.path.exists("user.csv"):
    with open("user.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(users)
    print("✅ Created user.csv with demo users.")

# Create quest.bin
if not os.path.exists("quest.bin"):
    with open("quest.bin", "wb") as f:
        pickle.dump(questions, f)
    print("✅ Created quest.bin with funny demo questions.")

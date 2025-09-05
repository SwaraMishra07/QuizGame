
---

# 📝 README.md

# 🎓 QuizMaster: Student–Teacher Quiz System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 About the Project
**QuizMaster** is a Python-based interactive quiz system designed for **students** and **teachers**.  
It features a **login system**, **question bank management**, and **performance tracking**, making it a great learning tool for classrooms or self-study.

---

## ✨ Features
- 🔑 **User Authentication** – Login, register, or continue in guest mode.
- 👨‍🏫 **Teacher Mode** – Add, manage, and view quiz questions.
- 👩‍🎓 **Student Mode** – Attempt quizzes and view results.
- 📚 **Question Bank** – Stored in a binary file (`quest.bin`) for persistence.
- 🏆 **Performance Board** – Tracks student scores and progress.
- ⌛ **Cinematic Slow-Print Effect** – Adds atmosphere to menus and messages.
- 🛠️ **Modular Structure** – Code separated into clear modules (`login.py`, `student.py`, `teacher.py`, `main.py`).

---

## 📂 Project Structure
```

quizmaster/
│── data/
│   └── user.csv         # Stores usernames & passwords
│── login.py             # Handles authentication & registration
│── student.py           # Quiz attempt & result tracking
│── teacher.py           # Manage question bank
│── utils.py             # Shared helpers (slow\_print, banners, etc.)
│── main.py              # Entry point (runs the app)
│── README.md            # Project documentation

````

---

## 🚀 How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/quizmaster.git
cd quizmaster
````

### 2️⃣ Ensure Python 3.x is Installed

👉 [Download Python](https://www.python.org/downloads/)

### 3️⃣ Run the App

```bash
python main.py
```

---

## 🧩 Usage

### Teacher

* Add or update quiz questions.
* View the complete question bank.

### Student

* Attempt quizzes and get instant results.
* View performance board after attempts.

### Guest Mode

* Attempt quizzes without saving results.

---

## 🌟 Future Improvements

* 🎒 **Inventory-like Rewards** – Unlock badges or items after quizzes.
* 🔀 **Multiple Quiz Modes** – Timed quiz, practice quiz, challenge quiz.
* 📊 **Graphical Reports** – Show score history using charts.
* 🌐 **Online Mode** – Host quizzes over a network or web.

---

## 🤝 Contributing

1. Fork the repo 🍴
2. Create a new branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Added new feature"`
4. Push branch: `git push origin feature-name`
5. Submit a Pull Request ✅

---

## ❤️ Acknowledgments

Made with Python and a love for teaching & learning 🎓✨

```

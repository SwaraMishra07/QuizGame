from login import login
from teacher import add_question, view_questions
from student import start_exam, show_result
from utils import banner, clear_screen

def main():
    clear_screen()
    banner("The Greatest Student-Teacher Quiz Interface")

    user = login()
    if not user:
        print("❌ Login failed. Exiting...")
        return

    while True:
        banner("Main Menu")
        print("1. Teacher - Add Question")
        print("2. Teacher - View Question Bank")
        print("3. Student - Take Exam")
        print("4. See Performance Board")
        print("5. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_question()
        elif choice == "2":
            view_questions()
        elif choice == "3":
            result = start_exam()
            show_result(result)
        elif opt == 4:
            performance_board()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()

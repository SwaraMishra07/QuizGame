import time
import os

def slow_print(text: str, delay: float = 0.02):
    """Prints text one character at a time for cinematic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    """Clears the console screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def banner(title: str):
    """Prints a decorative banner around the given title."""
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60 + "\n")
# util.py
import csv

RESULTS_FILE = "results.csv"

def save_result(username, name, cor, incor, skip, marks):
    """Save a student's result after the quiz."""
    file_exists = os.path.isfile(RESULTS_FILE)

    with open(RESULTS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:  # write header if file doesn't exist
            writer.writerow(["Username", "Name", "Correct", "Incorrect", "Skipped", "Score"])
        writer.writerow([username, name, cor, incor, skip, marks])


def performance_board():
    """Display all stored results as a leaderboard."""
    if not os.path.isfile(RESULTS_FILE):
        print("⚠️ No results found yet!")
        return

    with open(RESULTS_FILE, "r") as f:
        reader = csv.DictReader(f)
        results = list(reader)

    if not results:
        print("⚠️ No results found yet!")
        return

    # Sort by score (highest first)
    results.sort(key=lambda x: int(x["Score"]), reverse=True)

    print("\n================ PERFORMANCE BOARD ================\n")
    print(f"{'Rank':<5}{'Username':<20}{'Name':<15}{'Score':<10}{'Correct':<10}{'Incorrect':<12}{'Skipped':<10}")
    print("-" * 80)

    for idx, row in enumerate(results, start=1):
        print(f"{idx:<5}{row['Username']:<20}{row['Name']:<15}{row['Score']:<10}{row['Correct']:<10}{row['Incorrect']:<12}{row['Skipped']:<10}")

    print("=" * 80)

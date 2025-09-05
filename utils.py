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

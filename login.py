"""
login.py

Clean, modular login and registration utilities for the Quiz System.

Public function:
    login_user() -> (mode, username)
        mode: "user" or "guest"
        username: the username string (guest username if guest chosen)

Example:
    from login import login_user
    mode, username = login_user()
    if mode == "user":
        # registered user
    else:
        # guest mode
"""

import csv
import os

# Config: change if you want a different data folder / filename
DATA_DIR = "data"
USER_CSV = os.path.join(DATA_DIR, "user.csv")
CSV_HEADER = ["username", "password"]


# ----------------- Helpers -----------------

def ensure_data_dir():
    """Create the data directory if it doesn't exist."""
    if not os.path.isdir(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)


def ensure_user_csv():
    """
    Ensure the user.csv file exists and has a header row.
    If the file exists but lacks a header, this function will add one.
    """
    ensure_data_dir()
    if not os.path.exists(USER_CSV):
        # create with header
        with open(USER_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADER)
        return

    # check header presence
    with open(USER_CSV, "r", newline="", encoding="utf-8") as f:
        try:
            reader = csv.reader(f)
            first = next(reader, None)
        except Exception:
            first = None

    if first is None or first != CSV_HEADER:
        # Read existing rows then rewrite with proper header
        with open(USER_CSV, "r", newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f))
        # If the first row looks like data, keep it but add header
        with open(USER_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADER)
            # If original file had data rows, write them back (except header-like duplicates)
            for row in rows:
                if row == CSV_HEADER:
                    continue
                if len(row) >= 2:
                    writer.writerow([row[0].strip(), row[1].strip()])
                elif row:
                    # ignore malformed single-column rows
                    continue


def read_users():
    """Return a list of (username, password) tuples from user.csv (excluding header)."""
    ensure_user_csv()
    users = []
    with open(USER_CSV, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            uname = (r.get("username") or "").strip()
            pwd = (r.get("password") or "").strip()
            if uname and pwd:
                users.append((uname, pwd))
    return users


def user_exists(username):
    """Return True if username exists in user.csv (case-sensitive)."""
    users = read_users()
    return any(u == username for u, _ in users)


def validate_password(password):
    """
    Returns (is_valid: bool, message: str).
    Basic rules:
      - at least 4 characters
      - no commas (CSV delim)
      - no leading/trailing whitespace (we trim anyway)
    """
    pwd = password.strip()
    if len(pwd) < 4:
        return False, "Password must be at least 4 characters long."
    if "," in pwd:
        return False, "Password must not contain commas."
    return True, "OK"


def register_user(username, password):
    """Append a new user (username, password) to user.csv. Assumes validated inputs."""
    ensure_user_csv()
    with open(USER_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([username, password])


def authenticate(username, password):
    """Return True if credentials match a registered user."""
    users = read_users()
    return any(u == username and p == password for u, p in users)


# ----------------- Public API -----------------

def login_user():
    """
    Interactive login/registration flow.

    Returns:
        tuple (mode, username)
        - mode == "user": a registered user logged in
        - mode == "guest": guest mode (username is provided guest id)
    """
    ensure_user_csv()

    print("\n=== Welcome to the Quiz System Login ===\n")

    # ask for credentials
    while True:
        raw_user = input("Enter username (no commas): ").strip()
        if not raw_user:
            print("Username cannot be empty. Try again.")
            continue
        if "," in raw_user:
            print("Username must not contain commas. Try again.")
            continue
        username = raw_user
        break

    while True:
        raw_pwd = input("Enter password (min 4 chars, no commas): ").strip()
        is_valid, msg = validate_password(raw_pwd)
        if not is_valid:
            print("Invalid password:", msg)
            continue
        password = raw_pwd
        break

    # try authenticate
    if authenticate(username, password):
        print(f"\n✅ Logged in as registered user: {username}")
        return ("user", username)

    # user not found / incorrect credentials
    print("\n❌ Username/password not found or incorrect.")
    while True:
        choice = input("Do you want to register this account? (y/n) or type 'guest' to continue as guest: ").strip().lower()
        if choice in ("y", "yes"):
            if user_exists(username):
                print("That username already exists with a different password. Try logging in or choose another username.")
                # give option to retry login/register by returning control to caller
                return login_user()
            # register after validation
            register_user(username, password)
            print(f"\n✅ Registered new user: {username} (you are now logged in).")
            return ("user", username)
        elif choice in ("guest",):
            guest_name = f"guest_{username}"
            print(f"\n⚠️ Continuing in guest mode as {guest_name}. (Data will not be saved to the user database.)")
            return ("guest", guest_name)
        elif choice in ("n", "no"):
            # offer to retry or exit to caller — we loop back to login_user to restart
            print("Okay — let's try logging in again.")
            return login_user()
        else:
            print("Please type 'y' to register, 'n' to try logging in again, or 'guest' to continue as guest.")


# Optional: allow non-interactive programmatic usage
def login_with_credentials(username, password, auto_register=False):
    """
    Programmatic login helper.
    Returns ("user", username) if authenticated or registered (if auto_register True).
    Returns ("guest", username) if auto_register==False and not found.
    """
    username = username.strip()
    password = password.strip()
    is_valid, msg = validate_password(password)
    if not is_valid:
        raise ValueError(f"Invalid password: {msg}")

    if authenticate(username, password):
        return ("user", username)
    if auto_register:
        register_user(username, password)
        return ("user", username)
    return ("guest", f"guest_{username}")


# ----------------- If run directly (small demo) -----------------
if __name__ == "__main__":
    mode, user = login_user()
    print(f"\nMode: {mode}, User: {user}")

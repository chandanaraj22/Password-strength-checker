import re

def check_password_strength(password: str) -> str:
    """Return 'Weak', 'Medium', or 'Strong' based on simple heuristics."""
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[@$!%*?&#]", password) is None  # expand symbols if you like

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)

    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Medium"
    else:
        return "Weak"


if __name__ == "__main__":
    try:
        pwd = input("Enter your password: ")
        print(f"Password Strength: {check_password_strength(pwd)}")
    except KeyboardInterrupt:
        print("\nExiting...")

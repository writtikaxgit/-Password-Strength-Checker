import re

# Ask for user input
password = input("Enter your password: ")

# Define the criteria
min_length = 8
has_number = bool(re.search(r"\d", password))
has_uppercase = bool(re.search(r"[A-Z]", password))
has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

# Check password strength
if len(password) >= min_length and has_number and has_uppercase and has_special:
    print("Strong Password")
else:
    print("Weak Password")
    print("Missing criteria:")
    if len(password) < min_length:
        print("- Should be at least 8 characters long.")
    if not has_uppercase:
        print("- Include at least one uppercase letter.")
    if not has_number:
        print("- Include at least one number.")
    if not has_special:
        print("- Include at least one special character (e.g., !@#$%).")

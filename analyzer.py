import string

def analyze_password(password):
    score = 0
    suggestions = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make your password at least 8 characters long.")

    # Uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    # Lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    # Number
    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Include at least one number (0-9).")

    # Special Character
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add at least one special character (!,@,#,$,%,&, etc.).")

    # Common passwords
    common = [
        "password", "123456", "12345678",
        "password123", "admin", "qwerty"
    ]

    if password.lower() in common:
        suggestions.append("Avoid common passwords like 'password' or '123456'.")

    # Strength
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength, suggestions
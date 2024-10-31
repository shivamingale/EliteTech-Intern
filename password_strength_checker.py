import re

def assess_password_strength(password):
    # Initialize criteria flags
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Count how many criteria are met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria,
                        digit_criteria, special_char_criteria])
    
    # Determine strength based on criteria met
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, criteria_met

def provide_feedback(criteria_met):
    feedback = []
    if criteria_met < 5:
        feedback.append("Your password should be at least 8 characters long.")
    if criteria_met < 4:
        feedback.append("Include at least one uppercase letter.")
    if criteria_met < 3:
        feedback.append("Include at least one lowercase letter.")
    if criteria_met < 2:
        feedback.append("Include at least one digit.")
    if criteria_met < 1:
        feedback.append("Include at least one special character.")
    return feedback

def main():
    print("Password Strength Checker")
    password = input("Enter a password to assess its strength: ")
    strength, criteria_met = assess_password_strength(password)
    
    print(f"Password Strength: {strength}")
    
    if strength != "Very Strong":
        feedback = provide_feedback(criteria_met)
        print("Suggestions for improvement:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()

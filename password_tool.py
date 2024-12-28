import random
import string

def generate_password(length=12):
    """
    Generate a strong random password.
    :param length: Length of the password (default is 12).
    :return: Generated password as a string.
    """
    if length < 8:
        print("Warning: Password length should be at least 8 characters for better security.")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensure the password contains at least one of each type of character
    all_characters = lowercase + uppercase + digits + special_chars
    
    # Guarantee inclusion of at least one character of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password list to randomize order
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

def check_password_strength(password):
    """
    Check the strength of a password based on rules.
    :param password: Password to check.
    :return: Strength level and suggestions.
    """
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Calculate strength score
    score = 0
    if length >= 8: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1
    
    # Provide feedback
    if score == 5:
        return "Strong", "Your password is very strong!"
    elif score >= 3:
        return "Medium", "Consider adding more special characters, numbers, or length."
    else:
        return "Weak", "Your password is weak! Try adding uppercase letters, numbers, and special characters."

def main():
    print("\n==== Password Generator and Strength Checker ====")
    
    while True:
        print("\nChoose an option:")
        print("1. Generate a random password")
        print("2. Check password strength")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            try:
                length = int(input("Enter desired password length (min 8): "))
                if length < 4:
                    print("Password length must be at least 4 characters!")
                    continue
                generated_password = generate_password(length)
                print(f"Generated Password: {generated_password}")
            except ValueError:
                print("Please enter a valid number for length.")
                continue
        
        elif choice == '2':
            user_password = input("Enter your password to check its strength: ")
            strength, feedback = check_password_strength(user_password)
            print(f"Password Strength: {strength}")
            print(f"Feedback: {feedback}")
            
        elif choice == '3':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
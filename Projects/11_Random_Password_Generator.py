# modules and libraries
# program will ask you for the desired password length and what types of characters to include.

import random
import string

def generate(length, use_upper, use_digit, use_symbol):
    """
    Generates a random password based on specified criteria.
    """
    # base password
    pass1 = string.ascii_lowercase

    # Add other character types to the pool based on user's choice
    if use_upper:
        pass1 += string.ascii_uppercase
    if use_digit:
        pass1 += string.digits
    if use_symbol:
        pass1 += string.punctuation

    # Check if the character pool is empty
    if not pass1:
        return "Error: Please select at least one character type."

    password_list = random.choices(pass1, k=length)

    return "".join(password_list)

def main():
    print("🔑 Random Password Generator")
    print("---------------------------")

    try:
        length=int(input("Enter desired password length : "))
        if length<=0:
            print("Password length must be a positive number.")
            return

        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digit = input("Include digits? (y/n): ").lower() == 'y'
        use_symbol = input("Include symbols? (y/n): ").lower() == 'y'

        password=generate(length,use_upper, use_digit, use_symbol)

        print("\n---------------------------")
        print(f"✅ Generated Password: {password}")
        print("---------------------------")

    except ValueError:
        print("Invalid input. Please enter a valid number for the length.")

# This ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
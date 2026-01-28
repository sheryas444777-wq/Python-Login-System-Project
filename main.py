# ------------------------------------------
# PROJECT: Python Login System Project
# AUTHOR: Shreyas
# DESCRIPTION: Basic login system using file handling
# ------------------------------------------

import os

def sign_up():
    print("\n----- SIGN UP -----")
    
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    confirm = input("Confirm password: ")

    # Check if passwords match
    if password != confirm:
        print(" Passwords do not match!")
        return

    # Strong password rules
    if not any(c.islower() for c in password):
        print(" Password must contain at least one lowercase letter")
        return
    if not any(c.isupper() for c in password):
        print(" Password must contain at least one uppercase letter")
        return
    if len(password) < 8:
        print(" Password must be at least 8 characters long")
        return

    # Save user data in file
    file = open("login.txt", "w")
    file.write(username + "\n")
    file.write(password)
    file.close()

    print(" Account created successfully!")


def login():
    print("\n----- LOGIN -----")

    # Check if file exists
    if not os.path.exists("login.txt"):
        print(" No account found! Please Sign Up first.")
        return

    # Read saved credentials
    file = open("login.txt", "r")
    saved_username = file.readline().strip()
    saved_password = file.readline().strip()
    file.close()

    # Get login input
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Validate login
    if username == saved_username and password == saved_password:
        print("🎉 Login Successful! 🎉")
    else:
        print("❌ Invalid username or password")


def main_menu():
    while True:
        print("\n==============================")
        print("      LOGIN SYSTEM MENU")
        print("==============================")
        print("1️⃣  Sign Up")
        print("2️⃣  Login")
        print("3️⃣  Exit")
        print("------------------------------")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            login()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print(" Invalid Option! Try Again.")


# Run program
main_menu()


import re
import tkinter as tk
import random
import string

# Function to check the strength of a given password
def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    score = sum([length_criteria, upper_case_criteria, lower_case_criteria, digit_criteria, special_char_criteria])

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength

# Function to generate a random strong password
def generate_random_password():
    length = 12  # Length of the generated password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)  # Clear the current entry field
    password_entry.insert(0, password)  # Insert the generated password
    result_label.config(text="Generated a Strong Password!")  # Update the result label

# Function to check the strength of the entered password and display the result
def on_check_password():
    password = password_entry.get()
    strength = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")

# Function to toggle the visibility of the password
def toggle_password_visibility():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        toggle_button.config(text="Hide")
    else:
        password_entry.config(show='*')
        toggle_button.config(text="Show")

# Function to navigate to the password strength tester screen
def open_password_tester():
    main_menu.pack_forget()  # Hide the main menu
    password_tester_frame.pack()  # Show the password tester frame

# Main window setup
root = tk.Tk()
root.title("Password Strength Checker")

# Set window size
root.geometry("500x400")  # Width x Height

# Main menu frame
main_menu = tk.Frame(root)
main_menu.pack()

# Button to enter the password strength tester
enter_button = tk.Button(main_menu, text="Enter Strength Tester", command=open_password_tester)
enter_button.pack(pady=160)

# Password strength tester frame
password_tester_frame = tk.Frame(root)

# Label for password entry
password_label = tk.Label(password_tester_frame, text="Enter your password:")
password_label.pack(pady=10)

# Frame for password entry and toggle button
password_frame = tk.Frame(password_tester_frame)
password_frame.pack(pady=10)

# Entry field for password input
password_entry = tk.Entry(password_frame, show="*", width=30)
password_entry.pack(side=tk.LEFT)

# Toggle button to show/hide password
toggle_button = tk.Button(password_frame, text="Show", command=toggle_password_visibility)
toggle_button.pack(side=tk.LEFT, padx=10)

# Button to check the strength of the entered password
check_button = tk.Button(password_tester_frame, text="Check Strength", command=on_check_password)
check_button.pack(pady=10)

# Button to generate a strong random password
generate_button = tk.Button(password_tester_frame, text="Generate Strong Password", command=generate_random_password)
generate_button.pack(pady=10)

# Label to display the result of the password strength check
result_label = tk.Label(password_tester_frame, text="")
result_label.pack(pady=10)

# Button to navigate back to the main menu
back_button = tk.Button(password_tester_frame, text="Back to Main Menu", command=lambda: [password_tester_frame.pack_forget(), main_menu.pack()])
back_button.pack(pady=10)

# Run the application
root.mainloop()

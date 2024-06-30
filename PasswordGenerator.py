import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    exclude_duplicates = exclude_duplicates_var.get()
    include_spaces = include_spaces_var.get()

    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if include_spaces:
        characters += " "

    if not characters:
        messagebox.showerror("Error", "Select at least one character set!")
        return

    password = ""
    while len(password) < length:
        char = random.choice(characters)
        if exclude_duplicates and char in password:
            continue
        password += char

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Initialize main window
root = tk.Tk()
root.title("Password Generator")

# Password length
tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky=tk.W)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, columnspan=2, pady=5)
length_entry.insert(0, "12")

# Options for password
lowercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var).grid(row=1, column=0, sticky=tk.W)

uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).grid(row=2, column=0, sticky=tk.W)

numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=3, column=0, sticky=tk.W)

symbols_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=4, column=0, sticky=tk.W)

exclude_duplicates_var = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Exclude Duplicates", variable=exclude_duplicates_var).grid(row=5, column=0, sticky=tk.W)

include_spaces_var = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Include Spaces", variable=include_spaces_var).grid(row=6, column=0, sticky=tk.W)

# Generated password display
tk.Label(root, text="Generated Password:").grid(row=7, column=0, sticky=tk.W)
password_entry = tk.Entry(root, width=50)
password_entry.grid(row=7, column=1, columnspan=2, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=8, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet


class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Encryption Tool")

        # Key management
        self.key = None
        self.load_key()

        # Input field for text
        tk.Label(root, text="Enter Text:").grid(row=0, column=0, sticky=tk.W)
        self.input_text = tk.Text(root, height=10, width=50)
        self.input_text.grid(row=1, column=0, columnspan=2, pady=5)

        # Buttons
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.grid(row=2, column=0, pady=10)

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.grid(row=2, column=1, pady=10)

        # Output field for encrypted/decrypted text
        tk.Label(root, text="Output Text:").grid(row=3, column=0, sticky=tk.W)
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=4, column=0, columnspan=2, pady=5)

    def load_key(self):
        # Load the key from a file, or generate a new one
        try:
            with open("secret.key", "rb") as key_file:
                self.key = key_file.read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(self.key)

    def encrypt_text(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "No text entered")
            return

        fernet = Fernet(self.key)
        encrypted_text = fernet.encrypt(text.encode()).decode()
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, encrypted_text)

    def decrypt_text(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "No text entered")
            return

        fernet = Fernet(self.key)
        try:
            decrypted_text = fernet.decrypt(text.encode()).decode()
        except Exception as e:
            messagebox.showerror("Error", "Invalid encrypted text")
            return

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, decrypted_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()

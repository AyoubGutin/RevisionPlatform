import tkinter as tk
from tkinter import messagebox

validUsername = "username123"
validPassword = "password123"


class Authentication:
    def __init__(self):
        self.validUsername = "username123"
        self.validPassword = "password123"

    def authenticateUser(self, username, password):
        if username in cls.va



def login():
    """
    Function for retrieving a username and password from user
    and validating
    """

    enteredUsername = usernameEntry.get()
    enteredPassword = passwordEntry.get()

    if enteredUsername == validUsername and enteredPassword == validPassword:
        messagebox.showinfo("Authentication", "Login Successful")

    elif enteredUsername != validUsername or enteredPassword != validPassword:
        messagebox.showerror("Authentication", "Invalid Credentials")


# Main window for login
root = tk.Tk()
root.title("Login")

# Widgets (username, password)
tk.Label(root, text="Username: ").pack(pady=10)
usernameEntry = tk.Entry(root)
usernameEntry.pack(pady=10)

tk.Label(root, text="Password: ").pack(pady=10)
passwordEntry = tk.Entry(root)
passwordEntry.pack(pady=10)

loginButton = tk.Button(root, text="Login", command = login)
loginButton.pack(pady=20)

root.mainloop()

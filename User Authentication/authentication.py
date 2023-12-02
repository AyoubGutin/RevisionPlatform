import tkinter as tk
from tkinter import messagebox

#dummy user credentials to check validation
validUsername = "username123"
validPassword = "password123"

def authenticateUser():
    """
    1) Retrieves username and password from user
    2) Validates Credentials
    """
    enteredUsername = usernameEntry.get()
    enteredPassword = passwordEntry.get()

    if enteredUsername == validUsername and enteredPassword == validPassword:
        messagebox.showinfo("Authentication", "Login Successful")
    else:
        messagebox.showerror("Authentication", "Invalid Credentials")

# Create the main window for login
root = tk.Tk()
root.title("Login")

# Widgets (Username, Password, Login Button)
tk.Label(root, text="Username: ").pack(pady=5)
usernameEntry = tk.Entry(root)
usernameEntry.pack(pady=5)

tk.Label(root, text="Password: ").pack(pady=5)
passwordEntry = tk.Entry(root, show="*")
passwordEntry.pack(pady=5)

loginButton = tk.Button(root, text="Login", command=authenticateUser)
loginButton.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()


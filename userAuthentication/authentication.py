import tkinter as tk
from tkinter import messagebox

class UserAuthenticationManager:
    #dummy user credentials to check validation
    validUsers = {"user123": "pass123"}

    @classmethod
    def authenticateUser(cls, username, password):
        """
        class method for authenticating a user by comparing with dummy variable
        """

        if username in cls.validUsers and cls.validUsers[username] == password:
            return True
        return False

    @classmethod
    def registerUser(cls, username, password):
        if username not in cls.validUsers:
            cls.validUsers[username] = password
            return True
        return False

def authenticateUser():
    """
    1) Retrieves username and password from user
    2) Validates Credentials by calling on the class method authenticateuser
    """

    enteredUsername = usernameEntry.get()
    enteredPassword = passwordEntry.get()

    if UserAuthenticationManager.authenticateUser(enteredUsername, enteredPassword):
        messagebox.showinfo("Authentication", "Login Successful")
    else:
        messagebox.showerror("Authentication", "Invalid Credentials")

def registerUser():
    """
    1) retrieves username and password from user
    2) Validates this
    """
    enteredUsername = usernameEntry.get()
    enteredPassword = passwordEntry.get()
    confirmPassword = confirmPasswordEntry.get() # ** added confirmPassword entry

    if enteredPassword != confirmPassword:
        messagebox.showerror("Registration Error", "Passwords do not match") # ** added comparison to check passwords
    elif UserAuthenticationManager.registerUser(enteredUsername, enteredPassword):
        messagebox.showinfo("Registration", "Registration Successful")
    else:
        messagebox.showerror("Registration Error", "Username already exists")


# Create the main window for login
root = tk.Tk()
root.title("Register and Login Page ")

# Widgets (Username, Password, Login Button)
tk.Label(root, text="Username: ").pack(pady=5)
usernameEntry = tk.Entry(root)
usernameEntry.pack(pady=5)

tk.Label(root, text="Password: ").pack(pady=5)
passwordEntry = tk.Entry(root, show="*")
passwordEntry.pack(pady=5)

tk.Label(root, text ="Confirm Passowrd: ").pack(pady=5)
confirmPasswordEntry = tk.Entry(root, show="*")
confirmPasswordEntry.pack(pady=5)

loginButton = tk.Button(root, text="Login", command=authenticateUser)
loginButton.pack(pady=10)

# added new button for register
registerButton = tk.Button(root, text="Register", command=registerUser)
registerButton.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()


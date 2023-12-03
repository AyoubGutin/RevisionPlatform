import tkinter as tk
from tkinter import messagebox

class UserAuthenticationManager:
    #dummy user credentials to check validation
    validUsers = {"user123": {"password": "pass123", "email": "user123@gmail.com"}}

    @classmethod
    def authenticateUser(cls, username, password):
        """
        class method for authenticating a user by comparing with dummy variable
        """

        if username in cls.validUsers and cls.validUsers[username]["password"] == password:
            return True
        return False

    @classmethod
    def registerUser(cls, username, password, email):
        """
        class method for checking if username is not taken.
        """

        # Check if email is already associated with an account, checks if username is already associated.
        existingUsers = [user for user in cls.validUsers.values() if user["email"] == email]

        # Basic email validation
        if existingUsers or username in cls.validUsers or not email.endswith("@gmail.com"):
            return False # email or username exists or invalid email format

        # Basic username length check
        if len(password) < 8:
            return False # Invalid password

        if len(username) > 15:
            return False # Invalid username length

        elif username not in cls.validUsers:
            cls.validUsers[username] = {"password":password, "email":email }
            return True # registration accepted


def openRegistrationWindow():
    """
    Opens registration window for a better UI
    """
    registrationWindow = tk.Toplevel(selectionWindow)
    registrationWindow.title("Register")

    tk.Label(registrationWindow, text="Username: ").pack(pady=5)
    usernameEntry = tk.Entry(registrationWindow)
    usernameEntry.pack(pady=5)

    tk.Label(registrationWindow, text="Password: ").pack(pady=5)
    passwordEntry = tk.Entry(registrationWindow, show="*")
    passwordEntry.pack(pady=5)

    tk.Label(registrationWindow, text="Confirm Password: ").pack(pady=5)
    confirmPasswordEntry = tk.Entry(registrationWindow, show="*")
    confirmPasswordEntry.pack(pady=5)

    tk.Label(registrationWindow, text="Email: ").pack(pady=5)
    emailEntry = tk.Entry(registrationWindow)
    emailEntry.pack(pady=5)

    def registerUser():
        """
        1) retrieves username and password from user
        2) Validates this
        """
        enteredUsername = usernameEntry.get()
        enteredPassword = passwordEntry.get()
        confirmPassword = confirmPasswordEntry.get() # ** added confirmPassword entry
        enteredEmail = emailEntry.get()


        if enteredPassword != confirmPassword:
            messagebox.showerror("Registration Error", "Passwords do not match") # ** added comparison to check passwords
        elif UserAuthenticationManager.registerUser(enteredUsername, enteredPassword, enteredEmail):
            messagebox.showinfo("Registration", "Registration Successful")
            registrationWindow.destroy()
        else:
            messagebox.showerror("Registration Error", "Registration Failed, Try Again. ")

    registerButton = tk.Button(registrationWindow, text="Register", command=registerUser)
    registerButton.pack(pady=10)



def displayLogin():
    """
    1) Initialises login window
    1) Retrieves username and password from user
    2) Validates Credentials by calling on the class method authenticateuser
    """

    loginWindow = tk.Toplevel(selectionWindow)
    loginWindow.title("Login")

    tk.Label(loginWindow, text="Username: ").pack(pady=5)
    usernameEntry = tk.Entry(loginWindow)
    usernameEntry.pack(pady=5)

    tk.Label(loginWindow, text="Password: ").pack(pady=5)
    passwordEntry = tk.Entry(loginWindow, show="*")
    passwordEntry.pack(pady=5)


    def authenticationLogin():

        enteredUsername = usernameEntry.get()
        enteredPassword = passwordEntry.get()

        if UserAuthenticationManager.authenticateUser(enteredUsername, enteredPassword):
            messagebox.showinfo("Authentication", "Login Successful")
        else:
            messagebox.showerror("Authentication", "Invalid Credentials")

    loginButton = tk.Button(loginWindow, text="Login", command=authenticationLogin)
    loginButton.pack(pady=10)





# Create the main window for selection
selectionWindow = tk.Tk()
selectionWindow.title("Select Action ")


# Widgets (Login Button, Register Button)
loginButton = tk.Button(selectionWindow, text="Login", command=displayLogin)
loginButton.pack(pady=10)

registerButton = tk.Button(selectionWindow, text="Register", command=openRegistrationWindow)
registerButton.pack(pady=10)

# Start the Tkinter event loop
selectionWindow.mainloop()


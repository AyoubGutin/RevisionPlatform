import tkinter as tk
from tkinter import messagebox
import sqlite3   # RDMS


class UserAuthenticationManager:
    def __init__(self):
        self.conn = sqlite3.connect("user_database.db")
        self.createTables()

    def createTables(self):
        cursor = self.conn.cursor()

        # Create a table for students
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                email TEXT UNIQUE
            )
        """)

        # Create a table for teachers
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
                email TEXT UNIQUE
            )
        """)

        self.conn.commit()

    def authenticateUser(self, username, password):
        """
        class method for authenticating a user by comparing with database
        """
        cursor = self.conn.cursor()

        # Check for student login
        cursor.execute(f"SELECT * FROM students WHERE username=? AND password=?", (username, password))
        student = cursor.fetchone()

        if student:
            return "student", True

        # Check for teacher login
        cursor.execute("SELECT * FROM teachers WHERE username=? AND password=?", (username, password))
        teacher = cursor.fetchone()

        if teacher:
            return "teacher", True

        return None, False

    def registerUser(self, username, password, email, userType):
        """
        class method for validating a new account
        """

        cursor = self.conn.cursor()

        # Check if email is already associated with an account, checks if username is already associated.
        cursor.execute("SELECT * FROM students WHERE email=?", (email,))
        existingUser = cursor.fetchone()

        # Basic email validation
        if existingUser or not email.endswith("@gmail.com"):
            return False   # email exists or invalid email format

        # Basic username length check
        if len(password) < 8:
            return False   # Invalid password

        if len(username) > 15:
            return False   # Invalid username length

        cursor.execute("INSERT INTO students (username, password, email) VALUES (?, ?, ?", (username, password, email))
        self.conn.commit()
        return True

    def __del__(self):
        self.conn.close()

def openRegistrationWindow():
    """
    Opens registration window for a better UI
    Retrieves username and password from user
    Validates this by calling on registerUser()
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
        confirmPassword = confirmPasswordEntry.get()
        enteredEmail = emailEntry.get()

        if enteredPassword != confirmPassword:
            messagebox.showerror("Registration Error", "Passwords do not match") # Comparison to check passwords
        else:
            userType, success = UserAuthenticationManager.registerUser(enteredUsername, enteredPassword, enteredEmail)
            if success:
                messagebox.showinfo("Registration", f"Registration Successful for {userType.capitalize()}")

                if userType == "teacher":
                    registrationWindow.destroy() # Close teacher registration as not allowed

            else:
                messagebox.showerror("Registration Error", "Registration Failed, Try Again. ")

            registrationWindow.destroy()

    registerButton = tk.Button(registrationWindow, text="Register", command=registerUser)
    registerButton.pack(pady=10)


def displayLogin():
    """
    1) Initialises login window
    1) Retrieves username and password from user
    2) Validates Credentials by calling on the class method authenticateUser
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

        # Create instance of class
        authManager = UserAuthenticationManager()

        userType, success = authManager.authenticateUser(enteredUsername, enteredPassword)

        if success:
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

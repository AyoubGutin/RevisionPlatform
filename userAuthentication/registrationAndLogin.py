import tkinter as tk
from tkinter import messagebox
import sqlite3  # The relational database system I will be using, it is not server based, I can avoid paying costs
# this way. I will be using a graphical interface to view my tables.
import os  # Interacts  with the operating system, so I can create the database file in a path of my choice.


class UserManager:
    def __init__(self):
        # Specifies location of the place I want the database file to  be
        # This is as it was causing me issues as it was making the database file inside the authentication directory
        projectRoot = "C:\\Users\\washb\\PycharmProjects\\RevisionPlatform"
        dbPath = os.path.join(projectRoot, "user_database.db")

        try:
            self.conn = sqlite3.connect(dbPath)
            self.createTables()
        except sqlite3.Error as e:
            print("SQLITE ERROR", e)

    def createTables(self):
        """
        method for creating tables and checking if one exists
        """
        cursor = self.conn.cursor()

        # Create table for teachers - this is only needed once if a computer does not have a database file.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                teacherID INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                email TEXT UNIQUE
            )
        """)
        # Creates table for students - this is only needed once if a computer does not have a database file.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                studentID INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                email TEXT UNIQUE,
                teacherID INTEGER, 
                FOREIGN KEY (teacherID) REFERENCES teachers(teacherID)
            )
        """)

        self.conn.commit()

    def authenticateUser(self, username, password):
        """
        class method for authenticating a user by comparing with database
        """
        cursor = self.conn.cursor()

        # Attempts to fetch the username and password entered from the database and checks if it returns True.
        cursor.execute(f"SELECT * FROM students WHERE username=? AND password=?", (username, password))
        student = cursor.fetchone()

        if student:
            return "student", True

        # Attempts to fetch the username and password entered from the database and checks if it returns True.
        cursor.execute("SELECT * FROM teachers WHERE username=? AND password=?", (username, password))
        teacher = cursor.fetchone()

        if teacher:
            return "teacher", True

        return None, False

    def registerCheck(self, username, password, email, userType):
        """
        class method for validating a new account, responsible for checking database
        """

        cursor = self.conn.cursor()

        # Check if email is already associated with an account, checks if username is already associated.
        cursor.execute("SELECT * FROM students WHERE email=?", (email,))
        existingStudent = cursor.fetchone()

        print("Existing Student:", existingStudent)  # debug: check value

        # Basic email validation
        if existingStudent or not email.endswith("@gmail.com"):
            print("Email exists or Email is in wrong format")
            return False  # Email exists or invalid email format

        if len(password) < 8:
            print("Invalid password length")  # debug check
            return False  # Invalid password length

        if len(username) > 15:
            print("Invalid username")
            return False  # Invalid username length

        # If the userType is a student, it will be allowed to complete the register function and insert the values into
        # the database.
        if userType == "student":
            cursor.execute("SELECT teacherID FROM teachers ORDER BY teacherID LIMIT 1")
            teacherID = cursor.fetchone()
            teacherID = teacherID[0]  # extract teacherID from the tuple fetchone created
            print(teacherID)
            cursor.execute("INSERT INTO students (username, password, email, teacherID) VALUES (?, ?, ?, ?)",
                           (username, password, email, teacherID,))
        else:
            return False  # cannot register as a teacher or invalid user type.

        self.conn.commit()
        print("Registration successful")
        return True

    def closeConnection(self):
        if hasattr(self, "conn"):
            self.conn.close()


# Create instance of class so methods can be accessed
userAuth = UserManager()


def openRegistrationWindow():
    """
    Opens registration window for a better UI
    Displays input forms for username, password, email
    Validates this by calling on registerUser()
    """

    # Initialising widgets and input forms.
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
        1) retrieves username and password from user input
        2) Validates this by calling on the class method registerCheck() which deals with the database checks.
        """
        enteredUsername = usernameEntry.get()
        enteredPassword = passwordEntry.get()
        confirmPassword = confirmPasswordEntry.get()
        enteredEmail = emailEntry.get()

        # Checks if enteredPassword and confirmPassword are the same.
        if enteredPassword != confirmPassword:
            messagebox.showerror("Registration Error", "Passwords do not match")

        else:
            # Calls on registerCheck and success = True if database checks return True
            success = userAuth.registerCheck(enteredUsername, enteredPassword, enteredEmail, "student")
            if success:
                messagebox.showinfo("Registration", f"Registration Successful for {enteredUsername.upper()}")

            else:
                messagebox.showerror("Registration Error", "Registration Failed, Try Again. ")

            registrationWindow.destroy()
            userAuth.closeConnection()

    registerButton = tk.Button(registrationWindow, text="Register", command=registerUser)
    registerButton.pack(pady=10)


def displayLogin():
    """
    1) Initialises login window
    2) Retrieves username and password from user
    3) Validates Credentials by calling on the class method authenticateUser
    """

    # Sets up graphical interface for the login section when a user clicks on login in the homepage.
    loginWindow = tk.Toplevel(selectionWindow)
    loginWindow.title("Login")

    tk.Label(loginWindow, text="Username: ").pack(pady=5)
    usernameEntry = tk.Entry(loginWindow)
    usernameEntry.pack(pady=5)

    tk.Label(loginWindow, text="Password: ").pack(pady=5)
    passwordEntry = tk.Entry(loginWindow, show="*")
    passwordEntry.pack(pady=5)

    def loginUser():
        enteredUsername = usernameEntry.get()
        enteredPassword = passwordEntry.get()

        userType, success = userAuth.authenticateUser(enteredUsername, enteredPassword)

        if success:
            messagebox.showinfo("Authentication", "Login Successful")
        else:
            messagebox.showerror("Authentication", "Invalid Credentials")

    loginButton = tk.Button(loginWindow, text="Login", command=loginUser)
    loginButton.pack(pady=10)


# Create the main window for selection
bgColour = "#A9C6B8"
selectionWindow = tk.Tk()
selectionWindow.title("Select Action ")
selectionWindow.configure(bg=bgColour)
selectionWindow.geometry("600x400")


# Frame for buttons and headings
frame = tk.Frame(selectionWindow, bg=bgColour)
frame.pack(expand=True)

# Heading
headingColour = "#D9D9D9"
heading = tk.Label(frame, text="Select your choice", font=("Cairo", 16), bg=headingColour)
heading.pack()

# Widgets (Login Button, Register Button)
loginButton = tk.Button(frame, text="Login", command=displayLogin, height=5, width=15)
loginButton.pack(side="bottom", padx=15, pady=15)

registerButton = tk.Button(frame, text="Register", command=openRegistrationWindow, height=5, width=15)
registerButton.pack(side="top", padx=15, pady=15)

# Start the Tkinter event loop
selectionWindow.mainloop()

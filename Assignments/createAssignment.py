import tkinter as tk
import sqlite3
import os

bgColour = "#A9C6B8"
headingColour = "#D9D9D9"


class CreateNewAssignment:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Create New Assignment")
        parent.configure(bg=bgColour)
        parent.geometry("600x400")

        self.frame = tk.Frame(parent, bg=bgColour)
        self.frame.pack(expand=True)

        self.heading = tk.Label(self.frame, text="Enter Assignment", font=("Cairo", 16), bg=headingColour)
        self.heading.pack(fill="x")

        # Database connection
        projectRoot = "C:\\Users\\washb\\PycharmProjects\\RevisionPlatform"
        dbPath = os.path.join(projectRoot, "user_database.db")

        try:
            self.conn = sqlite3.connect(dbPath)
            self.createTable()
        except sqlite3.Error as e:
            print("SQLITE ERROR", e)

        # Entry for assignment
        self.assignmentTextEntry = tk.Entry(self.frame)
        self.assignmentTextEntry.pack(pady=10, padx=10)

        self.deadlineEntry = tk.Entry(self.frame)
        self.deadlineEntry.pack(pady=10, padx=10)

        # Button to create new assignment
        self.createAssignmentButton = tk.Button(self.frame, text="Create A New\n Assignment", command=self.createAssignment)
        self.createAssignmentButton.pack(padx=15, pady=15)

    def createTable(self):
        """
        Method for creating the assignment table
        """
        cursor = self.conn.cursor()

        # Create table for assignment if it doesn't exist
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS assignments (
                        assignmentID INTEGER PRIMARY KEY AUTOINCREMENT,
                        assignmentText TEXT UNIQUE,
                        deadline TEXT,
                        teacherID INTEGER,
                        FOREIGN KEY (teacherID) REFERENCES teachers(teacherID)
                    )
                """)
        self.conn.commit()

    def createAssignment(self):
        """
        Method to insert assignment into database
        """
        cursor = self.conn.cursor()

        # Retrieve data from entry form
        assignmentText = self.assignmentTextEntry.get()
        deadline = self.deadlineEntry.get()

        # There is only one teacher account.
        teacherID = 0

        cursor.execute("""
            INSERT INTO assignments(assignmentText, deadline, teacherID)
            VALUES (?, ?, ?)
        """, (assignmentText, deadline, teacherID))

        self.conn.commit()
        print("Assignment Created")
                       

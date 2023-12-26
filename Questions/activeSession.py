import tkinter as tk
import sqlite3
import os

bgColour = "#A9C6B8"
headingColour = "#D9D9D9"


class ActiveSession:
    def __init__(self, parent, difficultyLevel, studentID):
        self.parent = parent
        parent.title("Active Session")
        parent.configure(bg=bgColour)
        parent.geometry("600x400")

        self.difficultyLevel = difficultyLevel
        self.studentID = studentID

        self.frame = tk.Frame(parent, bg=bgColour)
        self.frame.pack(expand=True)

        self.heading = tk.Label(self.frame, text="Active Session", font=("Cairo", 16), bg=headingColour)
        self.heading.pack(fill="x")

        # Database connection for use in methods.
        projectRoot = "C:\\Users\\washb\\PycharmProjects\\RevisionPlatform"
        dbPath = os.path.join(projectRoot, "user_database.db")

        try:
            self.conn = sqlite3.connect(dbPath)
        except sqlite3.Error as e:
            print("SQLITE ERROR", e)

    def getQuestion(self):
        projectRoot = "C:\\Users\\washb\\PycharmProjects\\RevisionPlatform"
        dbPath = os.path.join(projectRoot, "user_database.db")

        try:
            conn = sqlite3.connect(dbPath)
        except sqlite3.Error as e:
            print("SQLITE ERROR", e)


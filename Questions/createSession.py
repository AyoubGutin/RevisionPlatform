import os
import tkinter as tk
import sqlite3

bgColour = "#A9C6B8"
headingColour = "#D9D9D9"


class CreateSession:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Create New Session")
        parent.configure(bg=bgColour)
        parent.geometry("600x400")

        self.frame = tk.Frame(parent, bg=bgColour)
        self.frame.pack(expand=True)

        self.heading = tk.Label(self.frame, text="New Session", font=("Cairo", 16), bg=headingColour)
        self.heading.pack(fill="x")

        # Database connection
        projectRoot = "C:\\Users\\washb\\PycharmProjects\\RevisionPlatform"
        dbPath = os.path.join(projectRoot, "user_database.db")

        try:
            self.conn = sqlite3.connect(dbPath)
            self.createTable()
        except sqlite3.Error as e:
            print("SQLITE ERROR", e)

    def createTable(self):
        """
        Method for creating the question table and question session table
        """
        cursor = self.conn.cursor()

        # Create table for questions if it doesn't exist
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS questions (
                        questionID INTEGER PRIMARY KEY AUTOINCREMENT,
                        questionText TEXT UNIQUE,
                        answer TEXT,
                        isCorrect BOOLEAN,
                        difficultyLevel INTEGER ,
                        points INTEGER
                    )
                """)
        self.conn.commit()

        # Create table for questionSession if it doesn't exist.
        cursor.execute("""
                     CREATE TABLE IF NOT EXISTS questionSession (
                         questionSessionID INTEGER PRIMARY KEY AUTOINCREMENT,
                         difficultyLevel INTEGER,
                         sessionTime FLOAT,
                         sessionPoints INTEGER,
                         studentID INTEGER,
                         questionID INTEGER,
                         FOREIGN KEY (studentID) REFERENCES students(studentID),
                         FOREIGN KEY (questionID) REFERENCES questions(questionID)
                     )
                 """)
        self.conn.commit()







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

        # Drop down menu for difficulty
        self.difficultyLabel = tk.Label(self.frame, text="Select Difficulty", bg=bgColour)
        self.difficultyLabel.pack(pady=10)

        self.difficultyVariable = tk.StringVar()
        self.difficultyVariable.set("1") # This is the default difficulty level

        difficultyOptions = ["1", "2", "3"]
        self.difficultyMenu = tk.OptionMenu(self.frame, self.difficultyVariable, *difficultyOptions)
        self.difficultyMenu.pack(pady=20)

        # Button for starting a session
        self.startSession = tk.Button(self.frame, text="Start Session!", command=self.insertQuestionSession)
        self.startSession.pack(side="bottom")

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
                        difficultyLevel TEXT,
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
                         FOREIGN KEY (studentID) REFERENCES students(studentID),
                     )
                 """)
        self.conn.commit()

        # Create table for QuestionSessionLinkQuestions table if it doesn't exist
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS questionSessionLinkQuestions
                    linkID INTEGER PRIMARY KEY AUTOINCREMENT,
                    questionSessionID INTEGER,
                    questionID INTEGER,
                    FOREIGN KEY questionSessionID REFERENCES questionSession(questionSessionID),
                    FOREIGN KEY questionID REFERENCES questions(questionID)""")

    def insertQuestionSession(self):
        difficultyLevel = int(self.difficultyVariable.get())

        cursor = self.conn.cursor()
        pass

    def startSession(self):
        pass







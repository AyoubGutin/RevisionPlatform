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
        self.frame.pack(fill="x")

        # UI elements
        self.heading = tk.Label(self.frame, text="Active Session", font=("Cairo", 16), bg=headingColour)
        self.heading.pack(fill="x")

        self.question = tk.Label(self.frame, text="", font=("Cairo", 16), bg=bgColour)
        self.question.pack(pady=20)

        self.indicator = tk.Label(self.frame, text="", font=("Cairo", 16), bg=bgColour)
        self.indicator.pack(pady=25)

        self.answerEntry = tk.Entry(self.frame, width=100)
        self.answerEntry.insert(0, "Enter Answer")
        self.answerEntry.pack(pady=10, padx=10)

        self.confirmAnswer = tk.Button(self.frame, text="Submit Answer", command=self.compareCorrectAnswer)
        self.confirmAnswer.pack()

        # Database connection for use in methods.
        projectRoot = "C:\\Users\\washb\\PycharmProjects\\RevisionPlatform"
        dbPath = os.path.join(projectRoot, "user_database.db")

        try:
            self.conn = sqlite3.connect(dbPath)
        except sqlite3.Error as e:
            print("SQLITE ERROR", e)

        self.getQuestion()

    def getQuestion(self):
        """
        Method for retrieving random question and a correct answer.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT questionText, answer FROM questions WHERE difficultyLevel = ? ORDER BY RANDOM() LIMIT 1", (self.difficultyLevel,))
        randomQuestion = cursor.fetchone()
        self.conn.close()

        self.question.config(text=randomQuestion[0])
        self.correctAnswer = randomQuestion[1]

    def compareCorrectAnswer(self):
        """
        Method for comparing correct answer with user answer
        """
        # Retrieve user answer
        userAnswer = self.answerEntry.get()

        if userAnswer == self.correctAnswer:
            self.indicator.config(text="Correct!")
        else:
            self.indicator.config(text=(f"Wrong, the answer is {self.correctAnswer}"))


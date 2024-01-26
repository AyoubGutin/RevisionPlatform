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

        self.endSessionButton = tk.Button(self.frame, text="End Session? ", command=self.endSession)
        self.endSessionButton.pack(side="right")

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
        cursor.execute("SELECT questionText, answer FROM questions WHERE difficultyLevel = ? ORDER BY RANDOM() LIMIT 1",
                       (self.difficultyLevel,))
        self.randomQuestion = cursor.fetchone()

        self.question.config(text=self.randomQuestion[0])
        self.correctAnswer = self.randomQuestion[1]

    def compareCorrectAnswer(self):
        """
        Method for:
        comparing correct answer with user answer
        """
        # Retrieve user answer
        userAnswer = self.answerEntry.get()

        cursor = self.conn.cursor()

        # Retrieve question and session ID
        cursor.execute("SELECT questionID FROM questions WHERE questionText = ?", (self.randomQuestion[0],))
        self.questionID = (cursor.fetchone()[0])

        cursor.execute("SELECT questionSessionID from questionSession ORDER BY questionSessionID DESC LIMIT 1")
        self.sessionID = (cursor.fetchone()[0])

        # Compare correct answer
        if userAnswer == self.correctAnswer:
            self.indicator.config(text="Correct!")
            cursor.execute("UPDATE questions SET isCorrect = 1 WHERE questionText = ?", (self.randomQuestion[0],))
            self.conn.commit()

        else:
            self.indicator.config(text=(f"Wrong, the answer is {self.correctAnswer}"))
            cursor.execute("UPDATE questions Set isCorrect = 0 WHERE questionText = ?", (self.randomQuestion[0],))
            self.conn.commit()

        cursor.execute("INSERT INTO questionSessionLinkQuestions(questionSessionID, questionID) VALUES (?, ?)",
                       (self.sessionID, self.questionID))
        self.conn.commit()

        self.getQuestion()

    def endSession(self):
        """
        Method to end session
        """
        self.getReport()
        self.parent.quit()

    def getReport(self):
        """
        Retrieves:
        - Amount of questions done
        - Amount of questions right
        - Questions that are wrong
        - Amount of points
        """
        cursor = self.conn.cursor()

        # Retrieve amount of questions
        cursor.execute("SELECT COUNT(linkID) FROM questionSessionLinkQuestions WHERE QuestionsessionID = ?", (self.sessionID,))
        questionCount = cursor.fetchone()[0]

        # Retrieve amount of questions right (get questionID -> from questionID find how many isCorrect = 1)
        cursor.execute("SELECT questionID FROM questionSessionLinkQuestions WHERE QuestionsessionID = ?", (self.sessionID,))
        questionIDs = cursor.fetchall()

        questionsRight = 0
        questionsWrongList = []

        for questionID in questionIDs:
            questionID = questionID[0]
            cursor.execute("SELECT isCorrect FROM questions WHERE questionID = ?", (questionID,))
            res = cursor.fetchone()[0]
            if res == 1:
                questionsRight += 1
            # Retrieve what questions are wrong
            else:
                cursor.execute("SELECT questionText FROM questions WHERE questionID = ?", (questionID,))
                res = cursor.fetchone()[0]
                questionsWrongList.append(res)

        points = questionsRight * self.difficultyLevel

        self.reportWindow(questionsRight, questionsWrongList, points)


    def reportWindow(self, questionsRight, questionsWrongList, points):
        """
        Method for displaying the report
        """
        reportWindow = tk.Toplevel(self.parent)
        reportWindow.title("Report")
        reportWindow.config(background=bgColour)
        reportWindow.geometry("600x400")

        questionsRightText = tk.Label(reportWindow, text=("You have gotten " + str(questionsRight) + " questions Right"), font=("Cairo", 16), bg=bgColour)
        questionsRightText.pack(pady=20)

        questionsWrongText = tk.Label(reportWindow, text=('Questions Wrong: \n'
                                                          , questionsWrongList), font=("Cairo", 16), bg=bgColour)
        questionsWrongText.pack(pady=20)

        pointsText = tk.Label(reportWindow, text=("You now have " + str(points) + " points"), font=("Cairo", 16), bg=bgColour)
        pointsText.pack(pady=20)










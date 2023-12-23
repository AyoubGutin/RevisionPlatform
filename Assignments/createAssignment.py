import tkinter as tk
import sqlite3
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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
        self.assignmentTextEntry = tk.Entry(self.frame, width=100)
        self.assignmentTextEntry.insert(0, "Enter Assignment Content")
        self.assignmentTextEntry.pack(pady=10, padx=10)

        self.deadlineEntry = tk.Entry(self.frame, width=100)
        self.deadlineEntry.insert(0, "Enter Deadline in the form\n dd/mm/yyyy")
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

        assignmentCreated = False
        if CreateNewAssignment.assignmentValidation(self, deadline):
            cursor.execute("""
                INSERT INTO assignments(assignmentText, deadline, teacherID)
                VALUES (?, ?, ?)
            """, (assignmentText, deadline, teacherID))

            self.conn.commit()
            print("Assignment Created")
            assignmentCreated = True
            self.assignmentNotification(cursor, assignmentText, deadline)

        else:
            print("Assignment NOT created")

    def assignmentNotification(self, cursor, assignmentText, deadline):
        """
        Nested function for the sending of assignments to students
        """

        # Retrieve emails from DB
        cursor.execute("SELECT email FROM students")
        emails = cursor.fetchall()
        self.conn.close()

        # Declare the sender email and password so Yahoo SMTP can access my account
        senderEmail = "reviseright@outlook.com"
        senderPassword = "EMUVBF6-Bbk-kZM"

        # Declare the email content
        subject = "New assignment"
        body = f"Assignment: {assignmentText} \nIt is due on {deadline}"

        # Configure Yahoo SMTP Server
        smtpServer = "smtp.office365.com"
        smtpPort = 587

        # Logging into SMTP Server
        server = smtplib.SMTP(smtpServer, smtpPort)
        server.starttls()
        server.login(senderEmail, senderPassword)

        # Go through each email retrieved and send an email
        for email in emails:
            message = MIMEMultipart()
            message["FROM"] = senderEmail
            message["TO"] = email[0]
            message["SUBJECT"] = subject
            message.attach(MIMEText(body, "plain"))

            # Send email
            server.sendmail(senderEmail, email[0], message.as_string())

        server.quit()

    def assignmentValidation(self, deadline):
        """
        Method to validate deadline entries
        """
        format = "%d/%m/%Y"
        check = True

        try:
            check = bool(datetime.strptime(deadline, format))
        except ValueError:
            check = False
        return check


                       

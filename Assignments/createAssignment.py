import tkinter as tk
import sqlite3
import os

bgColour = "#A9C6B8"
headingColour = "#D9D9D9"


class CreateNewAssignment:
    def __int__(self, parent):
        self.parent = parent
        parent.title("Create New Assignment")
        parent.configure(bg=bgColour)
        parent.geometry("600x400")

        self.frame = tk.Frame(parent, bg=bgColour)
        self.frame.pack(expand=True)

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
        Method for creating the assignment table
        """
        cursor = self.conn.cursor()

        # Create table for assignment if it doesn't exist
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS assignments (
                        assignmentID INTEGER PRIMARY KEY AUTOINCREMENT,
                        assignmentText TEXT UNIQUE,
                        deadline TEXT,
                        teacherID INTEGER
                        FOREIGN KEY (teacherID) REFERENCES teachers(teacherID)
                    )
                """)
        self.conn.commit()



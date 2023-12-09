import tkinter as tk

bgColour = "#A9C6B8"
headingColour = "#D9D9D9"


# Initialise class to encapsulate the logic specific to a student's homepage.
class StudentPage:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Homepage")
        parent.configure(bg=bgColour)
        parent.geometry("600x400")

        self.frame = tk.Frame(parent, bg=bgColour)
        self.frame.pack(expand=True)

        # Heading for homepage
        self.heading = tk.Label(self.frame, text="Homepage", font=("Cairo", 16), bg=headingColour)
        self.heading.pack(fill="x")

        # Widgets (Buttons)
        self.yourSessionsButton = tk.Button(self.frame, text="Your Sessions", height=5, width=15)
        self.yourSessionsButton.pack(side="left", padx=15, pady=15)

        self.createNewSessionButton = tk.Button(self.frame, text="Create New Session", height=5, width=15)
        self.createNewSessionButton.pack(side="left", padx=15, pady=15)

        self.newAssignmentsButton = tk.Button(self.frame, text="New Assignments", height=5, width=15)
        self.newAssignmentsButton.pack(side="right", padx=15, pady=15)


def openHomePage():
    root = tk.Tk()
    studentPage = StudentPage(root)
    root.mainloop()


openHomePage()

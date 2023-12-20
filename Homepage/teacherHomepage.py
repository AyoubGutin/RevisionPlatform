import tkinter as tk

bgColour = "#A9C6B8"
headingColour = "#D9D9D9"


# Initialise class to encapsulate the logic specific to a teacher's homepage.
class TeacherPage:
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
        self.yourStudentsButton = tk.Button(self.frame, text="Your Students", height=5, width=15,
                                            command=self.openYourStudentsButton)
        self.yourStudentsButton.pack(side="left", padx=15, pady=15)

        self.createNewAssignmentButton = tk.Button(self.frame, text="Create New\nAssignment", height=5, width=15,
                                                   command=self.openCreateNewAssignmentWindow)
        self.createNewAssignmentButton.pack(side="left", padx=15, pady=15)

        self.yourAssignmentsButton = tk.Button(self.frame, text="Your Assignments", height=5, width=15,
                                               command=self.openYourAssignmentsWindow)
        self.yourAssignmentsButton.pack(side="right", padx=15, pady=15)

    def openYourStudentsButton(self):
        yourStudentsWindow = tk.Toplevel(self.parent)
        YourStudentsWindow(yourStudentsWindow)

    def openCreateNewAssignmentWindow(self):
        createNewAssignmentWindow = tk.Toplevel(self.parent)
        CreateNewAssignmentWindow(createNewAssignmentWindow)

    def openYourAssignmentsWindow(self):
        yourAssignmentsWindow = tk.Toplevel(self.parent)
        YourAssignmentsWindow(yourAssignmentsWindow)


# Class to represent "Your Students" window
class YourStudentsWindow:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Your Students")
        parent.configure(bg=bgColour)
        parent.geometry("600x400")

        self.frame = tk.Frame(parent, bg=bgColour)
        self.frame.pack(expand=True)


# Class to represent "Create New Assignment" window
class CreateNewAssignmentWindow:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Create New Assignment")

        parent.configure(bg=bgColour)
        parent.geometry("600x400")

        self.frame = tk.Frame(parent, bg=bgColour)
        self.frame.pack(expand=True)


# Class to represent "Your Assignments" window.
class YourAssignmentsWindow:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Your Assignments")
        parent.configure(bg=bgColour)
        parent.geometry("600x400")

        self.frame = tk.Frame(parent, bg=bgColour)
        self.frame.pack(expand=True)


def openHomePage():
    root = tk.Tk()
    teacherPage = TeacherPage(root)
    root.mainloop()

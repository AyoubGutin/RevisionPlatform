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
        self.yourSessionsButton = tk.Button(self.frame, text="Your Sessions", height=5, width=15,
                                            command=self.openYourSessionsWindow)
        self.yourSessionsButton.pack(side="left", padx=15, pady=15)

        self.createNewSessionButton = tk.Button(self.frame, text="Create New Session", height=5, width=15,
                                                command=self.openCreateNewSessionWindow)
        self.createNewSessionButton.pack(side="left", padx=15, pady=15)

        self.newAssignmentsButton = tk.Button(self.frame, text="New Assignments", height=5, width=15,
                                              command=self.openNewAssignmentsWindow)
        self.newAssignmentsButton.pack(side="right", padx=15, pady=15)

    def openYourSessionsWindow(self):
        yourSessionsWindow = tk.Toplevel(self.parent)
        YourSessionsWindow(yourSessionsWindow)

    def openCreateNewSessionWindow(self):
        createNewSessionWindow = tk.Toplevel(self.parent)
        CreateNewSessionWindow(createNewSessionWindow)

    def openNewAssignmentsWindow(self):
        newAssignmentsWindow = tk.Toplevel(self.parent)
        NewAssignmentsWindow(newAssignmentsWindow)


# Class to represent "Your Sessions" window
class YourSessionsWindow:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Your Sessions")
        parent.configure(bg=bgColour)
        parent.geometry("600x400")

        self.frame = tk.Frame(parent, bg=bgColour)
        self.frame.pack(expand=True)


# Class to represent "New Session" window
class CreateNewSessionWindow:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Create New Session")
        parent.configure(bg=bgColour)
        parent.geometry("600x400")

        self.frame = tk.Frame(parent, bg=bgColour)
        self.frame.pack(expand=True)


# Class to represent "New Assignments" window.
class NewAssignmentsWindow:
    def __init__(self, parent):
        self.parent = parent
        parent.title("New Assignments")
        parent.configure(bg=bgColour)
        parent.geometry("600x400")

        self.frame = tk.Frame(parent, bg=bgColour)
        self.frame.pack(expand=True)


def openHomePage():
    root = tk.Tk()
    studentPage = StudentPage(root)
    root.mainloop()


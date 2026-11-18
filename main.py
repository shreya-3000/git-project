class CodeTracker:
    def __init__(self):
        print("Welcome to Your Code Tracker")
        self.solved = []
        self.WhatToTrack()
    def WhatToTrack(self):
        n = int(input("Press 1 to add Problem \nPress 2 to display solved problems \nPress 3 to delete problems solved \nEnter here: "))
        if n == 1:
            self.addProblem()
        elif n == 2:
            self.displaySolvedProb()
        elif n == 3:
            self.deleteProblem()
        else:
            print("Invalid Input!")
    def addProblem(self):
        p = input("Enter Problem name: ")
        self.solved.append(p)
        print(f"Problem {p} added successfully")
    def displaySolvedProb(self):
        if len(self.solved) == 0:
            print("No problems solved till now :(")
        print("Solved Problems-")
        for i, s in enumerate(self.solved):
            print(i, "->", s,"\n")
    def deleteProblem(self):
        n = int(input("Enter the problem number to be deleted: "))
        self.solved.pop(n-1)
c1 = CodeTracker()




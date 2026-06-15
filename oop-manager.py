class studentManager:
    def __init__(self):
        self.filename = "students.txt"
        
        with open(self.filename) as file:
            self.names = [name.strip() for name in file.readlines()]
 
    
    def updateFile(self):
        with open(self.filename, "w") as file:
            for name in self.names:
                file.write(name + "\n")
    
    def listStudents(self):
        for index, name in enumerate(self.names, start=1):
            print(f"{index}: {name}")

    def addStudent(self, name):
        self.names.append(name)
        self.updateFile()
    
    def findStudent(self, name):
        for currentName in self.names:
            if (currentName == name):
                print("Name found.")
                break
        else:
            print("Name not found.")

    def removeStudent(self, name):
        for index, currentName in enumerate(self.names):
            if (currentName == name):
                self.names.pop(index)
                print("Name has been removed.")
                self.updateFile()
                break
        else:
            print("Name does not exist.")

manager = studentManager()
print("\nWelcome to Student Manager v0.2")

while True:
    print("""Choose your option:
    1. List Students
    2. Add Student
    3. Find Student
    4. Remove Student
    5. Exit""")
    
    choice = input("Choose your option: ").lower().strip()
    print("\n")

    if choice in ["1", "liststudents"]:
        manager.listStudents()
    elif choice in ["2",  "addstudent"]:
        AddedName = input("Pick a name to add: ")
        manager.addStudent(AddedName)
    elif choice in ["3", "findstudent"]:
        FindName = input("Pick a name to find: ")
        manager.findStudent(FindName)
    elif choice in ["4",  "removestudent"]:
        RemoveName = input("Pick a name to remove: ")
        manager.removeStudent(RemoveName)
    elif choice in ["5",  "exit"]:
        break
    else:
        print("The command is invalid.")
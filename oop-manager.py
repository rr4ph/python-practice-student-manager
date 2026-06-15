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
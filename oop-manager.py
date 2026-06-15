class studentManager:
    def __init__(self):
        self.filename = "students.txt"
        
        with open(self.filename) as file:
            self.names = file.readlines()
    
    def updateFile(self):
        with open(self.filename, "w") as file:
            file.write(self.names)
    
    def listStudents(self):
        for index, name in enumerate(self.names, start=1):
            print(f"{index}: {name}")
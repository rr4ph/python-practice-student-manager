class studentManager:
    def __init__(self):
        self.filename = "students.txt"
        
        with open(self.filename) as file:
            self.names = [name.strip() for name in file.readlines()]
            print(self.names)
    
    def updateFile(self):
        with open(self.filename, "w") as file:
            for name in self.names:
                file.write(name + "\n")
    
    def listStudents(self):
        for index, name in enumerate(self.names, start=1):
            print(f"{index}: {name}")
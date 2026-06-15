class studentManager:
    def __init__(self):
        self.filename = "students.txt"
        
        with open(self.filename) as file:
            self.names = file.readlines()
    

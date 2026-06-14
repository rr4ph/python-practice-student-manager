def listStudents(names):
    for index, name in enumerate (names, start=1):
        print(f"{index}: {name}")

def addStudent(file, name):
    file.write(f"\n{name}")

def findStudent(names, name):
    for search in names:
        if (search.strip() == name):
            print("Found")
            break
    else:
        print("Not found")

def removeStudent(file, names, nameDelete):
    for index, name in enumerate(names):
        if (name.strip() == nameDelete):
            names.pop(index)
            for name in names:
                file.write(name)
            print(f"Name {nameDelete} has been deleted.")
            break
    else:
        for name in names:
                file.write(name)
        print("There is no such name in the file.")
    
with open("students.txt") as file:
    names = file.readlines();



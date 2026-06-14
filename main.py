def listStudents():
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





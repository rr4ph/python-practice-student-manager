def listStudents():
    for index, name in enumerate (names, start=1):
        print(f"{index}: {name}")

def addStudent(file, name):
    file.write(f"\n{name}")

def findStudent(list, name):
    for search in list:
        if (search.strip() == name):
            print("Found")
            break
    else:
        print("Not found")

def removeStudent(file, nameDelete):
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



import csv
from sys import argv

# -----------<For test>-----------#


def add_student(list, name, phone, email, group):
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)


def delete_student(list, name):
    for i, item in enumerate(list):
        if item["name"] == name:
            del list[i]
            return True
    return False

# -----------<Main>-----------#


def printAllList(list):
    for elem in list:
        strForPrint = "Student name is " + \
            elem["name"] + ",  Phone is " + elem["phone"] + \
            ",  Email is " + elem["email"] + ",  Group is " + elem["group"]
        print(strForPrint)


def addNewElement(list):
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")

    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return


def deleteElement(list):
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del list[deletePosition]
    return


def updateElement(list):
    name = input("Please enter name to be updated data: ")
    for i, item in enumerate(list):
        if item["name"] == name:
            upname = input("Enter new name: ")
            upphone = input("Enter new phone: ")
            upemail = input("Enter new email: ")
            upgroup = input("Enter new group: ")

            updateItem = {"name": upname, "phone": upphone,
                          "email": upemail, "group": upgroup}
            del list[i]

            insertPosition = 0
            for n in list:
                if upname > n["name"]:
                    insertPosition += 1
                else:
                    break
            list.insert(insertPosition, updateItem)
            print("Element update")
            return

    print("Element was not found")
    return

# ---------------------------------------------------


def readDataFromFile(studentList, inputfile):
    with open(inputfile) as file:
        reader = csv.DictReader(file)
        for row in reader:
            studentList.append(
                {"name": row["Studname"], "phone": row["Phone"], "email": row["Gmail"], "group": row["Group"]})


def saveData(studlist, inputfile):
    with open(inputfile, "w", newline="") as file:
        fieldnames = ["Studname", "Phone", "Gmail", "Group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in studlist:
            writer.writerow({
                "Studname": row["name"],
                "Phone":    row["phone"],
                "Gmail":    row["email"],
                "Group":    row["group"]
            })

# ---------------------------------------------------


def main():

    student_list = []

    if len(argv) < 2:
        print("Example: py Labs/Lab_02/Lab_02.py Labs/Lab_02/Lab_02.csv")
        return

    inputfile = argv[1]

    readDataFromFile(student_list, inputfile)
    while True:
        chouse = input(
            "Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(student_list)
                printAllList(student_list)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(student_list)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(student_list)
            case "P" | "p":
                print("List will be printed")
                printAllList(student_list)
            case "X" | "x":
                print("Saved data and Exit")
                saveData(student_list, inputfile)
                break
            case _:
                print("Wrong chouse")


if __name__ == "__main__":
    main()

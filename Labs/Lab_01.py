# List [Item1, Item2, Item3]
# Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name": "Adams Bob", "phone": "0631234567",
        "email": "damsbob@gmail.com", "group": "kb-242"},
    {"name": "Carter Emma", "phone": "0631234567",
        "email": "carteremma@gmail.com", "group": "kb-242"},
    {"name": "Green Jon",  "phone": "0631234567",
        "email": "greenjon@gmail.com", "group": "kb-242"},
    {"name": "Ross Zak",  "phone": "0631234567",
        "email": "rosszak@gmail.com", "group": "kb-242"}
]


def printAllList():
    for elem in list:
        strForPrint = "Student name is " + \
            elem["name"] + ",  Phone is " + elem["phone"] + \
            ",  Email is " + elem["email"] + ",  Group is " + elem["group"]
        print(strForPrint)


def addNewElement():
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


def deleteElement():
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
        # list.pop(deletePosition)
        del list[deletePosition]
    return

# ---------------------------------------------------


def updateElement():
    name = input("Please enter name to be updated data: ")
    for item in list:
        if item["name"] == name:
            item["name"] = input("Enter new name: ")
            item["phone"] = input("Enter new phone: ")
            item["email"] = input("Enter new email: ")
            item["group"] = input("Enter new group: ")

            list.sort(key=lambda x: x["name"])
            return

    print("Element was not found")
    return

# ---------------------------------------------------


def main():
    while True:
        chouse = input(
            "Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()

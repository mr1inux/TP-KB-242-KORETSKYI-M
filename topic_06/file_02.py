import csv


def readDataFromFile(listochek):
    with open("topic_06/Book.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            listochek.append(
                {"name": row["StudentName"], "mark": int(row["StudentMark"])})

# ------------------------------


def znch_sort():
    while True:
        m = input("za chum sortuvaty: ")
        if m != "name" and m != "mark":
            print("Errore! Try again.")
        else:
            return m


def sort(listochek, namekey):
    for elem in sorted(listochek, key=lambda x: x[namekey]):
        print(f"Name = {elem['name']}  mark = {elem["mark"]}")

# ------------------------------


def main():
    listochek = []
    с = znch_sort()
    readDataFromFile(listochek)
    sort(listochek, с)


main()

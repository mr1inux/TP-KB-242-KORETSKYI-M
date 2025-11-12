import requests

response = requests.get(
    "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")


def koshtu():
    while True:
        try:
            num = (input("Введіть суму:"))
            suma = float(num)
            return suma
        except ValueError:
            print(f"{num}: is not integer")


def main():

    while True:
        valyta = input("Виберіть валюту (EUR, USD, PLN): ").upper()

        if valyta == "EXIT":
            break

        elif valyta not in ["EUR", "USD", "PLN"]:
            print("Errore! Try again!")
            continue

        else:
            for elem in response.json():
                if elem['cc'] == valyta:
                    kurs = elem['rate']
                    break

        s = koshtu()
        result = kurs*s
        print(f"{s} {valyta} = {result} UAH"+"\n --------")


main()

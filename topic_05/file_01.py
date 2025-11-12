import random


def rund():
    return random.choice(["stone", "scissor", "paper"])


def battle(a, b):
    if a == b:
        return "It's a tie"
    elif (a == "stone" and b == "scissor") or \
         (a == "scissor" and b == "paper") or \
         (a == "paper" and b == "stone"):
        return "You are winner"
    else:
        return "You are loser"


def main():
    while True:
        word = input("Write your word: ")
        if word == "ex":
            print("Okey, exit.")
            break

        elif word not in ["stone", "scissor", "paper"]:
            print("Errore!")

        else:
            wrandom = rund()
            print(f"Computer's word: {wrandom}")
            r = battle(word, wrandom)
            print(r)
        print("-------------------")


main()

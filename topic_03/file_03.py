people = {'name': 'Max', 'age': 20, 'sex': 'male'}
print(people)

# оновлення або додавання нових пар ключ-значення
people.update({'age': 22, 'eyes': 'blue'})
print(people)

del people['name']  # видалення за ключем
print(people)

print(people.keys())  # отримати всі ключі
print(people.values())  # отримати всі значення
print(people.items())  # отримати всі пари ключ-значення

people.clear()
print(people)

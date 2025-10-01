l = ["Hello", "Max", 8, 3]

l.append(23)  # – додає елемент у кінець
print(l)

l.extend([9, 2])  # – розширює список іншим списком
print(l)

l.insert(1, 10)  # – вставляє елемент за індексом
print(l)

l.remove(3)  # – видаляє перше входження значення
print(l)

l.sort(key=str)  # – сортує список
print(l)

l.reverse()  # – змінює порядок елементів на зворотний
print(l)

l.copy()  # – створює копію списку
print(l)

l.clear()  # – очищає список
print(l)

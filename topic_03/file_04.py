type_list = [3, 2, 6, 8, 13, 76, 5]
type_list.sort()
print(type_list)
num = int(input('What is your number: '))


def vstavka(type_list, num):
    for i, e in enumerate(type_list):
        if num <= e:
            return i
    return len(type_list)


pos = vstavka(type_list, num)
print('Your position: ', pos)

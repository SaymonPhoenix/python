array = []
numbers = [1, 3, 5, 7, 9]
print(numbers)
numbers = [3, 6, 5.6, 'name']
print(numbers)
numbers = [33, 64, 5.67, [45.7, 7]]
print(numbers)

names = ['Кеша', 'Толик', 'Попугай']
print(names[1])
print(names[-1])
for name in names:
    print(name)

names.append('Жопкин')                                # Add in array
print(names)

names.pop()
print(names)                                         # Delete last

n = names.index('Толик')                          # получить индекс объекта массива
print(n)

print(len(names))                                   # Сколько объектов в массиве

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers.sort()                                      # Сортировка от меньшего к большему
print(numbers)
numbers.sort(reverse=True)                          # Сортировка от большего к меньшему
print(numbers)
numbers[1] = 'B'                                    # замена конкретного элемента массива
print(numbers)

leters = ['dsadaf', 'fggtrh', 'adlnkj', 'tkmcze']
leters.sort()
print(leters)
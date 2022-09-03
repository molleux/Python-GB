# Напишите программу, которая найдёт произведение пар чисел
# списка. Парой считаем первый и последний элемент, второй и
# предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] = > [12, 15, 16];
#         [2, 3, 5, 6] = > [12, 15]

lst = list(map(int, input('Введите целые чисела: ').split()))
result = []

if not len(lst) % 2:
    n = len(lst) // 2
else:
    n = len(lst) // 2 + 1

for i in range(n):
    mult = lst[i] * lst[(i + 1) * (-1)]
    result.append(mult)

print(result)

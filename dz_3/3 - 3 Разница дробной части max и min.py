# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
#     Пример:  [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 5, 10.01]
max_f = 1 / 10**30
min_f = 1

for i in lst:
    i = str(i)

    if i.find('.') > -1:
        point = i.find('.')
        fract = '0' + i[point:]
        fract = float(fract)

        if max_f < fract:
            max_f = fract
        if min_f > fract:
            min_f = fract

difference = max_f - min_f
print(difference)

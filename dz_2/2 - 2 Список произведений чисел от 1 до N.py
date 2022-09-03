#  Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.#
#     Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#  Реализуйте алгоритм перемешивания списка.

from random import shuffle

n = int(input('Введите целое число:'))

my_list = []
figure = 1
for i in range(1, n + 1):
    figure *= i
    my_list.append(figure)

print(my_list)

shuffle(my_list)
print(my_list)
help(shuffle)

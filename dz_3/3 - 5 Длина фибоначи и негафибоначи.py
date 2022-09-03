# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#   Пример: - для k = 8 список будет выглядеть так:
#     [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fib(m):
    if m in [1, 2]:
        return 1
    else:
        return fib(m - 1) + fib(m - 2)


input_nam = int(input("Введите целое число: "))
my_list = []

for i in range(1, input_nam + 1):
    my_list.append(fib(i))

nega = []
len_my_list = len(my_list)
for i in my_list[-1:0]:
    i *= (-1)


print(my_list)




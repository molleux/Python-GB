# Вывести на экран числа от -N до N

n2 = int(input('Введите число целое положитнльное число: '))

# через for
n1 = n2 * -1
for i in range(n1, n2 + 1):
    print(i, end=',')

# генератор
picture = (i for i in range(n1, n2 + 1))
print('\n', *picture)

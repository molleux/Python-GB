# Найти максимальное из пяти чисел

row = list(map(int, input('введите 5 целых чисел больше 0 через пробел: ').split()))
my_max = 0

for i in row:
    if my_max < i:
        my_max = i

print(f'Максимальное число: {my_max}')

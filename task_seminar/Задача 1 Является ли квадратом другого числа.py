# По двум заданным числам проверить является ли одно квадратом второго

a, b = int(input('введите число а:')), int(input('введите число b:'))

if a**2 == b:
    input(f'число b:{b} является квадратом числа a:{a}')
elif b**2 == a:
    input(f'число a:{a} является квадратом числа b:{b}')
else:
    print('ни одно из чисел квадратом дркгого не является')

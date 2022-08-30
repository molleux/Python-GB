# 3  Найти расстояние между двумя точками пространства


def modul(z):  # выравниваем числа по модулю
    if z < 0:
        z = z * (-1)
    return z


x1 = float(input('введите координаты 1й точки по X: '))
y1 = float(input('введите координаты 1й точки по Y: '))
x2 = float(input('введите координаты 2й точки по X: '))
y2 = float(input('введите координаты 2й точки по Y: '))

x_distance = x1 - x2
x_distance = modul(x_distance)

y_distance = y1 - y2
y_distance = modul(y_distance)

distance = (x_distance**2 + y_distance**2)**0.5

print(f'Растоляние между точками графика: {distance}')

# 2 Указав номер четверти прямоугольной системы координат, показать
#  допустимые значения координат для точек этой четверти

q = int(input('введите номер четверти системы координат (целое число от 1 - 4): '))
x = None
if q == 1:
    print('Для ввода значения X доступны числа от 0 до + бесконечности')
    print('Для ввода значения Y доступны числа от 0 до + бесконечности')
elif q == 2:
    print('Для ввода значения Х доступны числа от - бесконечности до 0')
    print('Для ввода значения Y доступны числа от 0 до + бесконечности')
elif q == 3:
    print('Для ввода значения Х доступны числа от - бесконечности до 0')
    print('Для ввода значения Y доступны числа от - бесконечности до 0')
elif q == 4:
    print('Для ввода значения X доступны числа от 0 до + бесконечности')
    print('Для ввода значения Y доступны числа от - бесконечности до 0')

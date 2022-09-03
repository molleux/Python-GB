#  Напишите программу, которая будет преобразовывать десятичное
#  число в двоичное.
#    Пример:
#           - 45 -> 101101
#           - 3 -> 11
#           - 2 -> 10


def get_binary_num(sourse_num):
    binary_num = ''
    while sourse_num > 1:
        if sourse_num % 2 == 0:
            binary_num += '0'
            sourse_num = sourse_num // 2
            if sourse_num == 1:
                binary_num += '1'
        else:
            binary_num += '1'
            sourse_num = sourse_num // 2
            if sourse_num == 1:
                binary_num += '1'

    return binary_num[::-1]


sourse_num = int(input('Введите целое число: '))
print(get_binary_num(sourse_num))

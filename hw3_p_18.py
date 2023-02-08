# Задача № 18 Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

from random import randint
try:
    n = int(input('Введите размер массива: '))

    user_array = [randint(1, 10) for i in range(n)]
    print('Ваш массив:', user_array)

    x = int(input('Введите интересующее вас число: '))

    min = abs(x - user_array[0])
    result = user_array[0]

    for i in range(1, len(user_array)):
        if min > abs(user_array[i] - x):
            min = abs(user_array[i] - x)
            result = user_array[i]
    print(f'Самый близкий к заданному числу элемент массива со значением: {result}')
except:
    print('Вы ввели неверные данные!')

# Задача № 20 Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

char_dict = {'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1,'о': 1, 'р': 1, 'с': 1, 'т': 2, 'к': 2, 'л': 2, 'м': 2, 'п': 2,
             'у': 2, 'д': 2, 'б': 3, 'г': 3, 'ё': 3, 'ь': 3, 'я': 3, 'й': 4, 'ы': 4, 'ж': 5, 'з': 5, 'х': 5, 'ц': 5,
             'ч': 5, 'ш': 8, 'э': 8, 'ю': 8, 'ф': 8, 'щ': 10, 'ъ': 10}
try:
    user_word = input('Напишите ваше слово кириллическими строчными буквами : ')
    user_lst = list(user_word)

    sum = 0
    for i in user_lst:
        a = char_dict[i]
        sum = sum + a
    print(f'Сумма ваших очков составляет: {sum}!')
except:
    print('Вы ввели неверные данные!')
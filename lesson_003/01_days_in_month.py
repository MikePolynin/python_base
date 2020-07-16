# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if month <= 0 or month > 12:
    print('Некорректный ввод')
else:
    if month == 2:
        print('В месяце 28 дней')
    elif month <= 7:
        if month % 2 == 0:
            print('В месяце 30 дней')
        else:
            print('В месяце 31 день')
    else:
        if month % 2 == 0:
            print('В месяце 31 день')
        else:
            print('В месяце 30 дней')
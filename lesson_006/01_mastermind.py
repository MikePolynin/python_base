# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.

#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

from lesson_006.mastermind_engine import guess_the_number, check_the_number

guess_the_number()
# TODO, предлагаю этот вызов функции реализовать в начале цикла while. Сейчас дважды вызываем. А так будем один раз.
user_input_list = []
steps = 0
while True:

    # TODO, Михаил, предлагаю создать специальную функцию для проверки числа пользователяь
    #  Она будет просить ввести число и проверять, если число введено неправильно, просить заново, если правильное,
    #  то возвращать это число. И далее будем использовать его в функции check_the_number.
    user_input = input('Input your number:')
    if len(user_input) != 4:
        print('Wrong input')
        continue
    elif user_input[0].isdigit() and int(user_input[0]) == 0:
        print('Wrong input')
        continue
    for element in user_input:
        if not element.isdigit():
            print('Wrong input')
            break
        elif int(element) in user_input_list:
            print('Wrong input')
            user_input_list.clear()
            break
        else:
            user_input_list.append(int(element))
    if len(user_input_list) == 4:
        steps += 1
        print(check_the_number(user_input_list))
        if check_the_number(user_input_list)['bulls'] == 4:
            print('You win by', steps, 'steps')
            user_input_list.clear()
            steps = 0
            one_more_game = input('One more game? y/n')
            if one_more_game == 'y' or 'Y':
                guess_the_number()
                continue
        user_input_list.clear()

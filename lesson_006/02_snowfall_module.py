# -*- coding: utf-8 -*-

import simple_draw as sd
import lesson_006.snowfall as snowfall
# import python_base.lesson_006.snowfall as snowfall

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
snowfall.create_snowflakes(5)
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    snowfall.drawing_snowflakes(sd.background_color)
    #  сдвинуть_снежинки()
    snowfall.moving_snowflakes()
    #  нарисовать_снежинки_цветом(color)
    snowfall.drawing_snowflakes(sd.COLOR_WHITE)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    snowfall.fallen_snowflakes()
    if snowfall.fallen_snowflake_list:
        snowfall.delete_snowflake()
        snowfall.create_snowflakes(len(snowfall.fallen_snowflake_list))
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

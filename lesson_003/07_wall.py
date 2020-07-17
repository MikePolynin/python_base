# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

for row, y in enumerate(range(0, 625, 52)):
    # if row % 2 == 0:
    #     x = 0
    # else:
    #     x = -51

    x = 0 if row % 2 == 0 else - 51  # Тернарный оператор позволяет сократить кол-во кода

    for x in range(x, 613, 102):
        left_bottom = simple_draw.get_point(x, y)
        right_top = simple_draw.get_point(x + 100, y + 50)
        simple_draw.rectangle(left_bottom, right_top, simple_draw.COLOR_RED, 1)

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

simple_draw.pause()

# зачёт!

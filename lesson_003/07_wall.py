# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

x_start = 0
# TODO, получилась лишняя переменная, как я понял, она необходима для определения чётности ряда.
#  Можно использовать следующую схему "for row, y in enumerate(range(0, 625, 52)):" где row это номер строки
#  Далее будем определять, чётный он или нет и исходя из этого, принимать решение начинать с 0 или -51

for y in range(0, 625, 52):
    for x in range(x_start, 613, 102):
        left_bottom = simple_draw.get_point(x, y)
        right_top = simple_draw.get_point(x + 100, y + 50)
        simple_draw.rectangle(left_bottom, right_top, simple_draw.COLOR_RED, 1)
    if x_start == 0:
        x_start -= 51
    else:
        x_start = 0

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

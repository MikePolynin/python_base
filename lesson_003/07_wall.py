# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# TODO, Михаил, стена получилась отличная. Сделайте пожалуйста в 1 часть. Сейчас у нас в 2. =)
#  Алгоритм отрисовки в подсказке ниже.
for y in range(0, 625, 104):
    for x in range(0, 613, 102):
        left_bottom = simple_draw.get_point(x, y)
        right_top = simple_draw.get_point(x + 100, y + 50)
        simple_draw.rectangle(left_bottom, right_top, simple_draw.COLOR_RED, 1)

for y in range(52, 625, 104):
    for x in range(-51, 613, 102):
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

# -*- coding: utf-8 -*-

import simple_draw

simple_draw.resolution = (1500, 600)

x = 578
y = 181
color = simple_draw.random_color()

# TODO, переменные выше необходимо передать как параметры функции
#  sd.resolution лучше убрать. Иначе может возникнуть непонятный сдвиг в основном файле.
def smiles_draw():
    point = simple_draw.get_point(x, y)
    simple_draw.circle(point, 50, color)

    left_eye_point = simple_draw.get_point(x - 20, y + 10)
    simple_draw.circle(left_eye_point, 10, color)

    right_eye_point = simple_draw.get_point(x + 20, y + 10)
    simple_draw.circle(right_eye_point, 10, color)

    point_1 = simple_draw.get_point(x - 30, y - 20)
    point_2 = simple_draw.get_point(x - 10, y - 35)
    point_3 = simple_draw.get_point(x + 10, y - 35)
    point_4 = simple_draw.get_point(x + 30, y - 20)
    smile_point = [point_1, point_2, point_3, point_4]
    simple_draw.lines(smile_point, color)

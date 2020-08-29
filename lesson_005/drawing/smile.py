# -*- coding: utf-8 -*-

import simple_draw

color_1 = simple_draw.COLOR_WHITE
color_2 = simple_draw.background_color


def smiles_draw(x, y, color):
    global color_1
    global color_2

    point = simple_draw.get_point(x, y)
    simple_draw.circle(point, 50, color)

    left_eye_point = simple_draw.get_point(x - 20, y + 10)
    simple_draw.circle(left_eye_point, 10, color)

    point_1 = simple_draw.get_point(x - 30, y - 20)
    point_2 = simple_draw.get_point(x - 10, y - 35)
    point_3 = simple_draw.get_point(x + 10, y - 35)
    point_4 = simple_draw.get_point(x + 30, y - 20)
    smile_point = [point_1, point_2, point_3, point_4]
    simple_draw.lines(smile_point, color)

    right_eye_point = simple_draw.get_point(x + 20, y + 10)
    start_point = simple_draw.get_point(x + 10, y + 10)
    end_point = simple_draw.get_point(x + 30, y + 10)

    if color_1 != simple_draw.background_color:
        color_1 = color
    else:
        color_2 = color
    simple_draw.line(start_point, end_point, color_1)
    simple_draw.circle(right_eye_point, 10, color_2)
    color_1, color_2 = color_2, color_1

# -*- coding: utf-8 -*-

import simple_draw

view = [1]  # TODO почему именно список, а не, к примеру, True/False? Но это не понадобится, лучше использовать две
#  глобальные переменные цветов (см. ниже)

color_1 = simple_draw.COLOR_WHITE
color_2 = simple_draw.COLOR_WHITE


def smiles_draw(x, y, color):
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

    global color_1
    global color_2

    simple_draw.line(start_point, end_point, color_1)
    simple_draw.circle(right_eye_point, 10, color_2)
    color_1 = color
    color_2 = simple_draw.background_color
    color_1, color_2 = color_2, color_1
    # TODO Используйте такуй трюк для смены цветов: color1, color2 = color2, color1 и дублировать код не понадобится

# -*- coding: utf-8 -*-

import simple_draw as sd

view = [1]


def draw_rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    radius = 950
    center = sd.get_point(600, -50)
    for color in rainbow_colors:
        sd.circle(center, radius, color, 10)
        radius += 12
    # TODO тут по сути меняется только цвет и view.
    #  Предлагаю использовать тернарные операторы. Это сократит кол-во кода. Был пример в Lesson 03 07_wall.py
    #  Попробуйте пожалуйста. В таком случае, цикл можно будет вынести за пределы блока if/else
    if view[0] == 0:
        for radius_white in range(940, 1025, 12):
            sd.circle(center, radius_white, sd.background_color, 2)
        view[0] = 1
    else:
        for radius_white in range(940, 1025, 12):
            sd.circle(center, radius_white, sd.COLOR_WHITE, 2)
        view[0] = 0

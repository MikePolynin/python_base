# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1500, 600)
# TODO sd.resolution лучше убрать. Иначе может возникнуть непонятный сдвиг в основном файле.

def draw_rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    radius = 950
    for color in rainbow_colors:
        center = sd.get_point(600, -50)
        sd.circle(center, radius, color, 10)
        radius += 12

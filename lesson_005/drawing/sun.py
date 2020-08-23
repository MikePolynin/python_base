# -*- coding: utf-8 -*-
import simple_draw


def draw_sun(x, y):
    center = simple_draw.get_point(x, y)
    simple_draw.circle(center, 40, simple_draw.COLOR_YELLOW, 0)
    angle = 0
    for line in range(1, 9):
        vector = simple_draw.get_vector(center, angle, 90, 5)
        vector.draw()
        angle = 45 * line
        simple_draw.sleep(0.1)

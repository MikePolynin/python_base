# -*- coding: utf-8 -*-
import simple_draw

dif_angle = [0]


def draw_sun(x, y):
    angle = 0
    center = simple_draw.get_point(x, y)
    for line in range(0, 10):
        vector = simple_draw.get_vector(center, angle, 90, 5)
        vector.draw(simple_draw.background_color)
        angle = 45 * line + dif_angle[0]
    simple_draw.circle(center, 40, simple_draw.COLOR_YELLOW, 0)
    dif_angle[0] += 30
    for line in range(1, 9):
        vector = simple_draw.get_vector(center, angle, 90, 5)
        vector.draw()
        angle = 45 * line + dif_angle[0]

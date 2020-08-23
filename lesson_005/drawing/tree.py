# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_branches(start_point, dif_angle=90, length=100):
    if length < 10:
        return
    vector = sd.get_vector(start_point, dif_angle, length)
    vector.draw()

    dif_angle_1 = sd.random_number(18, 42)
    dif_length_1 = sd.random_number(6, 9) / 10
    dif_angle_2 = sd.random_number(18, 42)
    dif_length_2 = sd.random_number(6, 9) / 10
    draw_branches(vector.end_point, vector.angle + dif_angle_1, vector.length * dif_length_1)
    draw_branches(vector.end_point, vector.angle - dif_angle_2, vector.length * dif_length_2)

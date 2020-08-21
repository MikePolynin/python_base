# -*- coding: utf-8 -*-

import simple_draw

simple_draw.resolution = (1500, 600)

for row, y in enumerate(range(0, 313, 52)):
    x = 400 if row % 2 == 0 else 351

    for x in range(x, 715, 102):
        left_bottom = simple_draw.get_point(x, y)
        right_top = simple_draw.get_point(x + 100, y + 50)
        simple_draw.rectangle(left_bottom, right_top, simple_draw.COLOR_RED, 1)

roof_point_list = [simple_draw.get_point(351, 364), simple_draw.get_point(578, 450), simple_draw.get_point(806, 364)]
simple_draw.lines(roof_point_list, simple_draw.COLOR_RED, 1)

left_bottom = simple_draw.get_point(351, 0)
right_top = simple_draw.get_point(806, 362)
simple_draw.rectangle(left_bottom, right_top, simple_draw.COLOR_RED, 1)

left_bottom_window = simple_draw.get_point(518, 121)
right_top_window = simple_draw.get_point(638, 241)
simple_draw.rectangle(left_bottom_window, right_top_window, simple_draw.COLOR_RED, 5)
simple_draw.rectangle(left_bottom_window, right_top_window, simple_draw.background_color, 0)

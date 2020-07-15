# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.
x_start = 50
x_end = 350

for color in rainbow_colors:
    start_point = sd.get_point(x_start, 50)
    end_point = sd.get_point(x_end, 450)
    sd.line(start_point, end_point, color, 4)
    x_start += 5
    x_end += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
radius = 300
for color in rainbow_colors:
    center = sd.get_point(300, -50)
    sd.circle(center, radius, color, 10)
    radius += 12

sd.pause()

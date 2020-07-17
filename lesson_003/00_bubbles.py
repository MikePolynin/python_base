# -*- coding: utf-8 -*-
import random

import simple_draw as sd

# isinstance()
sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(point, radius)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def draw_bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius, color)


# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    draw_bubble(point, 5, sd.COLOR_YELLOW)

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 401, 150):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        draw_bubble(point, 5, sd.COLOR_YELLOW)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(5, 15)
    color = sd.random_color()
    draw_bubble(point, step, color)

sd.pause()

# зачёт!

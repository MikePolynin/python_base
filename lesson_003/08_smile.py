# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smiles_draw(x, y, color):
    point = simple_draw.get_point(x, y)
    simple_draw.circle(point, 50, color)

    left_eye_point = simple_draw.get_point(x - 20, y + 10)
    simple_draw.circle(left_eye_point, 10, color)

    right_eye_point = simple_draw.get_point(x + 20, y + 10)
    simple_draw.circle(right_eye_point, 10, color)

    point_1 = simple_draw.get_point(x - 30, y - 20)
    point_2 = simple_draw.get_point(x - 10, y - 35)
    point_3 = simple_draw.get_point(x + 10, y - 35)
    point_4 = simple_draw.get_point(x + 30, y - 20)
    smile_point = [point_1, point_2, point_3, point_4]
    simple_draw.lines(smile_point, color)


for _ in range(10):
    x, y = simple_draw.random_point().x, simple_draw.random_point().y
    smiles_draw(x, y, simple_draw.random_color())

simple_draw.pause()

# зачёт!

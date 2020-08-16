# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def draw_triangle(x, y, angle, length):
    start_point = sd.get_point(x, y)
    vector_0 = sd.get_vector(start_point, angle, length)
    vector_1 = sd.get_vector(vector_0.end_point, angle + 120, length)
    vector_2 = sd.get_vector(vector_1.end_point, angle + 240, length)
    vector_0.draw()
    vector_1.draw()
    vector_2.draw()


def draw_square(x, y, angle, length):
    start_point = sd.get_point(x, y)
    vector_0 = sd.get_vector(start_point, angle, length)
    vector_1 = sd.get_vector(vector_0.end_point, angle + 90, length)
    vector_2 = sd.get_vector(vector_1.end_point, angle + 180, length)
    vector_3 = sd.get_vector(vector_2.end_point, angle + 270, length)
    vector_0.draw()
    vector_1.draw()
    vector_2.draw()
    vector_3.draw()


def draw_pentagram(x, y, angle, length):
    start_point = sd.get_point(x, y)
    vector_0 = sd.get_vector(start_point, angle, length)
    vector_1 = sd.get_vector(vector_0.end_point, angle + 72, length)
    vector_2 = sd.get_vector(vector_1.end_point, angle + 144, length)
    vector_3 = sd.get_vector(vector_2.end_point, angle + 216, length)
    vector_4 = sd.get_vector(vector_3.end_point, angle + 288, length)
    vector_0.draw()
    vector_1.draw()
    vector_2.draw()
    vector_3.draw()
    vector_4.draw()


def draw_six_angles(x, y, angle, length):
    start_point = sd.get_point(x, y)
    vector_0 = sd.get_vector(start_point, angle, length)
    vector_1 = sd.get_vector(vector_0.end_point, angle + 60, length)
    vector_2 = sd.get_vector(vector_1.end_point, angle + 120, length)
    vector_3 = sd.get_vector(vector_2.end_point, angle + 180, length)
    vector_4 = sd.get_vector(vector_3.end_point, angle + 240, length)
    vector_5 = sd.get_vector(vector_4.end_point, angle + 300, length)
    vector_0.draw()
    vector_1.draw()
    vector_2.draw()
    vector_3.draw()
    vector_4.draw()
    vector_5.draw()


def shape_select(shapes):
    print('Available shapes are:')
    for key, value in shapes.items():
        print(key, ':', value.get('fig_name'))
    input_shape = input('Select a shape: ')
    while input_shape not in shapes:
        print('Wrong input')
        print('Available shapes are:')
        for key, value in shapes.items():
            print(key, ':', value.get('fig_name'))
        input_shape = input('Select a shape: ')

    shapes.get(input_shape).get('func')(300, 300, 20, 150)


all_shapes = {'0': {'fig_name': 'треугольник', 'func': draw_triangle},
              '1': {'fig_name': 'квадрат', 'func': draw_square},
              '2': {'fig_name': 'пятиугольник', 'func': draw_pentagram},
              '3': {'fig_name': 'шестиугольник', 'func': draw_six_angles}}

shape_select(all_shapes)

sd.pause()

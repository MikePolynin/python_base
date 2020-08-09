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


def shape_select():
    shapes_count = 0  # TODO Лишняя переменная
    shapes_numbers = {}  # TODO Лишняя переменная
    for key, value in enumerate(all_shapes):
        shapes_numbers[key] = value
        shapes_count += 1
    # TODO Лишнее действие
    # TODO Словарь all_shapes в таком случае будет как глобальная переменная.
    #  Чтобы не путаться сейчас лучше отказаться от награмождения функциями =)
    available_shapes_print(shapes_numbers)
    input_shape = input('Select a shape: ')

    while int(input_shape) >= shapes_count:
        # TODO лучше проверять наличие ключа в словаре. Ключами сделать цифры 1, 2 и т.д.
        #  Если ввести слово - получаем ошибку. Скрипт перестаёт работать.
        print('Incorrect input')
        available_shapes_print(shapes_numbers)
        input_shape = input('Select a shape: ')
        # TODO Если ключами будут цифры, то таких тяжёлых вычислений не будет =)
    shapes_numbers[int(input_shape)].get('func')(300, 300, 20, 150)


def available_shapes_print(shapes):
    print('Available shapes are:')
    for shape_key, shape_value in shapes.items():
        print(shape_key, ':', shape_value.get('fig_name'))


all_shapes = [{'fig_name': 'треугольник', 'func': draw_triangle},
              {'fig_name': 'квадрат', 'func': draw_square},
              {'fig_name': 'пятиугольник', 'func': draw_pentagram},
              {'fig_name': 'шестиугольник', 'func': draw_six_angles}]

shape_select()

sd.pause()

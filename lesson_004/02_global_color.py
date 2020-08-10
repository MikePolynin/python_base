# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def draw_triangle(x, y, angle, length, draw_color):
    start_point = sd.get_point(x, y)
    vector_0 = sd.get_vector(start_point, angle, length)
    vector_1 = sd.get_vector(vector_0.end_point, angle + 120, length)
    vector_2 = sd.get_vector(vector_1.end_point, angle + 240, length)
    vector_0.draw(draw_color)
    vector_1.draw(draw_color)
    vector_2.draw(draw_color)


def draw_square(x, y, angle, length, draw_color):
    start_point = sd.get_point(x, y)
    vector_0 = sd.get_vector(start_point, angle, length)
    vector_1 = sd.get_vector(vector_0.end_point, angle + 90, length)
    vector_2 = sd.get_vector(vector_1.end_point, angle + 180, length)
    vector_3 = sd.get_vector(vector_2.end_point, angle + 270, length)
    vector_0.draw(draw_color)
    vector_1.draw(draw_color)
    vector_2.draw(draw_color)
    vector_3.draw(draw_color)


def draw_pentagram(x, y, angle, length, draw_color):
    start_point = sd.get_point(x, y)
    vector_0 = sd.get_vector(start_point, angle, length)
    vector_1 = sd.get_vector(vector_0.end_point, angle + 72, length)
    vector_2 = sd.get_vector(vector_1.end_point, angle + 144, length)
    vector_3 = sd.get_vector(vector_2.end_point, angle + 216, length)
    vector_4 = sd.get_vector(vector_3.end_point, angle + 288, length)
    vector_0.draw(draw_color)
    vector_1.draw(draw_color)
    vector_2.draw(draw_color)
    vector_3.draw(draw_color)
    vector_4.draw(draw_color)


def draw_six_angles(x, y, angle, length, draw_color):
    start_point = sd.get_point(x, y)
    vector_0 = sd.get_vector(start_point, angle, length)
    vector_1 = sd.get_vector(vector_0.end_point, angle + 60, length)
    vector_2 = sd.get_vector(vector_1.end_point, angle + 120, length)
    vector_3 = sd.get_vector(vector_2.end_point, angle + 180, length)
    vector_4 = sd.get_vector(vector_3.end_point, angle + 240, length)
    vector_5 = sd.get_vector(vector_4.end_point, angle + 300, length)
    vector_0.draw(draw_color)
    vector_1.draw(draw_color)
    vector_2.draw(draw_color)
    vector_3.draw(draw_color)
    vector_4.draw(draw_color)
    vector_5.draw(draw_color)


# TODO, Михали, пожалуйста, обратите внимание, если ввести не число, спрашивать цвет наш скрипт перестаёт.
#  Предлагаю уйти от проверок input_color.isdigit() и int(input_color) >= len(all_colors) и просто проверять
#  наличие ключа в словаре all_colors. Вложенных циклов while быть не должно =)
#  Ввёл 14 и получил ошубку "ValueError: invalid color name".
#  Воможно, ошибка в этой части кода "drawing(all_colors.get(input_color)[0])".



def color_select():
    print('Available colors are:')
    for key, value in all_colors.items():
        print(key, ':', value[0])
    input_color = input('Select a color: ')
    while input_color.isdigit():
        while int(input_color) >= len(all_colors):
            print('Wrong number')
            print('Available colors are:')
            for key, value in all_colors.items():
                print(key, ':', value[0])
            input_color = input('Select a color: ')
            break
        else:
            drawing(all_colors.get(input_color)[0])  # или так all_colors[input_color][0]
            break
    else:
        print('Incorrect input')
        exit()


def drawing(selected_color):
    draw_triangle(150, 100, 0, 100, selected_color)
    draw_square(150, 250, 10, 100, selected_color)
    draw_pentagram(400, 150, 20, 100, selected_color)
    draw_six_angles(400, 350, 30, 100, selected_color)


all_colors = {
    '0': ['white', sd.COLOR_WHITE],
    '1': ['black', sd.COLOR_BLACK],
    '2': ['red', sd.COLOR_RED],
    '3': ['orange', sd.COLOR_DARK_ORANGE],
    '4': ['yellow', sd.COLOR_DARK_YELLOW],
    '5': ['cyan', sd.COLOR_CYAN],
    '6': ['blue', sd.COLOR_BLUE],
    '7': ['purple', sd.COLOR_DARK_PURPLE],
    '8': ['dark yellow', sd.COLOR_DARK_YELLOW],
    '9': ['dark orange', sd.COLOR_DARK_ORANGE],
    '10': ['dark red', sd.COLOR_DARK_RED],
    '11': ['dark green', sd.COLOR_DARK_GREEN],
    '12': ['dark cyan', sd.COLOR_DARK_CYAN],
    '13': ['dark blue', sd.COLOR_DARK_BLUE],
    '14': ['dark purple', sd.COLOR_DARK_PURPLE]}

color_select()

sd.pause()

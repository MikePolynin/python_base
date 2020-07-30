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

# TODO, Михаил, интересных ход =)
#  предлагаю фрактал не использовать в этом упрожнении. Запутанно получилось и с ошибками.
def color_select():
    input_color = input('Select a color: ')

    if int(input_color) >= colors_count:
        print('Incorrect input')
        color_select()
    else:
        selected_color = all_colors.get(colors_numbers.get(int(input_color)))
        drawing(selected_color)


def drawing(selected_color):
    draw_triangle(150, 100, 0, 100, selected_color)
    draw_square(150, 250, 10, 100, selected_color)
    draw_pentagram(400, 150, 20, 100, selected_color)
    draw_six_angles(400, 350, 30, 100, selected_color)


all_colors = {
    'white': sd.COLOR_WHITE,
    'black': sd.COLOR_BLACK,
    'red': sd.COLOR_RED,
    'orange': sd.COLOR_DARK_ORANGE,
    'yellow': sd.COLOR_DARK_YELLOW,
    'cyan': sd.COLOR_CYAN,
    'blue': sd.COLOR_BLUE, # Михаил, пожалуйста, обратите внимание, как правильно переносить текст при создании словаря.
              'purple': sd.COLOR_DARK_PURPLE, 'dark yellow': sd.COLOR_DARK_YELLOW, 'dark orange': sd.COLOR_DARK_ORANGE,
              'dark red': sd.COLOR_DARK_RED, 'dark green': sd.COLOR_DARK_GREEN, 'dark cyan': sd.COLOR_DARK_CYAN,
              'dark blue': sd.COLOR_DARK_BLUE, 'dark purple': sd.COLOR_DARK_PURPLE}

colors_count = 0
colors_numbers = {}

print('Available colors are:')

# TODO, вместо циклов for и фракталов, для выбора пользователя, организуйте пожалуйста цикл while.
# TODO, введёное число пользователя, лучше использовать как ключи нашего словаря.
#  В таком случае, будет проще проверять наличие нужного цвета. Будет меньше лишних переменных.
#  В случае неправильного ввода пользователя, пожалуйста выводите повторно список цветов.
# for key, value in all_colors.items():  # по словарю в цикле лучше с items()
for color in enumerate(all_colors.keys()):
    colors_numbers[color[0]] = color[1]
    print(color[0], ':', color[1])
    colors_count += 1

color_select()

sd.pause()

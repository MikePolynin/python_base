# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# def draw_triangle(x, y, angle, length):
#     start_point = sd.get_point(x, y)
#     vector_0 = sd.get_vector(start_point, angle, length)
#     vector_1 = sd.get_vector(vector_0.end_point, angle + 120, length)
#     vector_2 = sd.get_vector(vector_1.end_point, angle + 240, length)
#     vector_0.draw()
#     vector_1.draw()
#     vector_2.draw()
#
#
# def draw_square(x, y, angle, length):
#     start_point = sd.get_point(x, y)
#     vector_0 = sd.get_vector(start_point, angle, length)
#     vector_1 = sd.get_vector(vector_0.end_point, angle + 90, length)
#     vector_2 = sd.get_vector(vector_1.end_point, angle + 180, length)
#     vector_3 = sd.get_vector(vector_2.end_point, angle + 270, length)
#     vector_0.draw()
#     vector_1.draw()
#     vector_2.draw()
#     vector_3.draw()
#
#
# def draw_pentagram(x, y, angle, length):
#     start_point = sd.get_point(x, y)
#     vector_0 = sd.get_vector(start_point, angle, length)
#     vector_1 = sd.get_vector(vector_0.end_point, angle + 72, length)
#     vector_2 = sd.get_vector(vector_1.end_point, angle + 144, length)
#     vector_3 = sd.get_vector(vector_2.end_point, angle + 216, length)
#     vector_4 = sd.get_vector(vector_3.end_point, angle + 288, length)
#     vector_0.draw()
#     vector_1.draw()
#     vector_2.draw()
#     vector_3.draw()
#     vector_4.draw()
#
#
# def draw_six_angles(x, y, angle, length):
#     start_point = sd.get_point(x, y)
#     vector_0 = sd.get_vector(start_point, angle, length)
#     vector_1 = sd.get_vector(vector_0.end_point, angle + 60, length)
#     vector_2 = sd.get_vector(vector_1.end_point, angle + 120, length)
#     vector_3 = sd.get_vector(vector_2.end_point, angle + 180, length)
#     vector_4 = sd.get_vector(vector_3.end_point, angle + 240, length)
#     vector_5 = sd.get_vector(vector_4.end_point, angle + 300, length)
#     vector_0.draw()
#     vector_1.draw()
#     vector_2.draw()
#     vector_3.draw()
#     vector_4.draw()
#     vector_5.draw()
#
#
# draw_square(100, 100, 0, 100)
# draw_pentagram(100, 350, 10, 100)
# draw_triangle(450, 100, 20, 100)
# draw_six_angles(450, 350, 30, 100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# зачёт первой части, пожалуйста, приступайте ко второй!

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)


def drawing(fig_start_point, start_angel, corners_numbers, length):
    fig_angel = 360 / corners_numbers
    start_point = fig_start_point
    for _ in range(0, corners_numbers - 1):
        vector = sd.get_vector(start_point, start_angel, length)
        vector.draw()
        start_point = vector.end_point
        start_angel = vector.angle + fig_angel
    sd.line(start_point, fig_start_point)


def draw_triangle(x, y, angle, length):
    start_point = sd.get_point(x, y)
    drawing(start_point, angle, 3, length)


def draw_square(x, y, angle, length):
    start_point = sd.get_point(x, y)
    drawing(start_point, angle, 4, length)


def draw_pentagram(x, y, angle, length):
    start_point = sd.get_point(x, y)
    drawing(start_point, angle, 5, length)


# Если объединить x и y в одну переменную. Упростим жизнь пользователю =)
def draw_six_angles(x, y, angle, length):
    start_point = sd.get_point(x, y)
    drawing(start_point, angle, 6, length)


draw_square(100, 100, 0, 100)
draw_pentagram(100, 350, 10, 100)
draw_triangle(450, 100, 20, 100)
draw_six_angles(450, 350, 30, 100)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()

# зачёт!

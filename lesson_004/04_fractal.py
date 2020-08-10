# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# 1
#
#
# def draw_branches(start_point, angle, length):
#     vector_0 = sd.get_vector(start_point, angle + 30, length)
#     vector_1 = sd.get_vector(start_point, angle - 30, length)
#     vector_0.draw()
#     vector_1.draw()

# 2
#
#
# def draw_branches(start_point, angle, length):
#     if length < 10:
#         return
#     vector = sd.get_vector(start_point, angle, length)
#     vector.draw()
#     draw_branches(vector.end_point, vector.angle + 30, vector.length * 0.75)
#     draw_branches(vector.end_point, vector.angle - 30, vector.length * 0.75)
#

# 3
#
#
# root_point = sd.get_point(300, 30)
# draw_branches(root_point, 90, 100)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.resolution = (1200, 600)


def draw_branches(start_point, angle, length):
    if length < 10:
        return
    vector = sd.get_vector(start_point, angle, length)
    vector.draw()

    # TODO, Михаил, пожалуйста, обратите внимание. 1ый угол желательно всегда указывать 90 градусов.
    #  Первая веточка всегда вверх. А все последующие должны рандомно изменяться отталкиваясь от него.
    #  Сейчас просто меняются рандомно.

    dif_angle_1 = sd.random_number(18, 42)
    dif_length_1 = sd.random_number(6, 9) / 10
    dif_angle_2 = sd.random_number(18, 42)
    dif_length_2 = sd.random_number(6, 9) / 10
    draw_branches(vector.end_point, vector.angle + dif_angle_1, vector.length * dif_length_1)
    draw_branches(vector.end_point, vector.angle - dif_angle_2, vector.length * dif_length_2)


root_point = sd.get_point(300, 30)
draw_branches(root_point, 90, 100)
sd.pause()
# Пожалуйста, приступайте к усложнённому заданию.
# зачёт!

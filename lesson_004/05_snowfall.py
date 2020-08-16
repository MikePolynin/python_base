# -*- coding: utf-8 -*-
import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 5

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# snowflakes_list = []
# for i in range(N):
#     snowflakes_list.append(
#         [sd.random_number(50, 550), sd.random_number(450, 600), sd.random_number(10, 70), sd.random_number(10, 20)])
#
# while True:
#     sd.clear_screen()
#     for snowflake_index, snowflake in enumerate(snowflakes_list):
#         snowflake[0] += sd.random_number(-5, 5)
#         point = sd.get_point(snowflake[0], snowflake[1])
#         sd.snowflake(point, snowflake[2])
#         if snowflake[1] <= 0:
#             snowflakes_list[snowflake_index] = [
#                 sd.random_number(50, 550),
#                 sd.random_number(450, 600),
#                 sd.random_number(10, 70),
#                 sd.random_number(1, 10)
#             ]
#         snowflake[1] -= snowflake[3]
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
# sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл

# зачёт первой части. Пожалуйста, приступайте ко второй.

# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

snowflakes_list = []
for i in range(N):
    snowflakes_list.append(
        [sd.random_number(50, 550), sd.random_number(550, 650), sd.random_number(10, 70), sd.random_number(10, 20)])

while True:
    sd.start_drawing()
    for snowflake_index, snowflake in enumerate(snowflakes_list):
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(point, snowflake[2], sd.background_color)
        if snowflake[1] <= snowflake[2]:
            snowflakes_list[snowflake_index] = [
                sd.random_number(50, 550),
                sd.random_number(550, 650),
                sd.random_number(10, 70),
                sd.random_number(1, 10)
            ]
        snowflake[1] -= snowflake[3]
        snowflake[0] += sd.random_number(-5, 5)
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(point, snowflake[2])
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()

# зачёт!

# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1500, 600)


# TODO, Михаил, пожалуйста, реализуйте этот код в виде функции. Её импортируем в 04_painting.py
N = 5

snowflakes_list = []
for i in range(N):
    snowflakes_list.append(
        [sd.random_number(5, 200), sd.random_number(550, 650), sd.random_number(10, 70), sd.random_number(10, 20)])

while True:
    sd.start_drawing()
    for snowflake_index, snowflake in enumerate(snowflakes_list):
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(point, snowflake[2], sd.background_color)
        if snowflake[1] <= snowflake[2]:
            snowflakes_list[snowflake_index] = [
                sd.random_number(5, 200),
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

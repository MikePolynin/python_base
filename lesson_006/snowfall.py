# -*- coding: utf-8 -*-
import simple_draw as sd

snowflakes = {}
fallen_snowflake_list = []


def create_snowflakes(n):
    global snowflakes
    if fallen_snowflake_list:
        for i in fallen_snowflake_list:
            snowflake_name = 'snowflake_' + str(i)
            snowflakes[snowflake_name] = [sd.random_number(5, 200),
                                          sd.random_number(550, 650),
                                          sd.random_number(10, 70),
                                          sd.random_number(10, 20)]
        fallen_snowflake_list.clear()
    else:
        for i in range(n):
            snowflake_name = 'snowflake_' + str(i)
            snowflakes[snowflake_name] = [sd.random_number(5, 200),
                                          sd.random_number(550, 650),
                                          sd.random_number(10, 70),
                                          sd.random_number(10, 20)]


def drawing_snowflakes(color):
    global snowflakes
    for value in snowflakes.values():
        point = sd.get_point(value[0], value[1])
        sd.snowflake(point, value[2], color)


def moving_snowflakes():
    global snowflakes
    for value in snowflakes.values():
        value[1] -= value[3]
        value[0] += sd.random_number(-5, 5)


def fallen_snowflakes():
    global snowflakes
    global fallen_snowflake_list
    for key, value in snowflakes.items():
        if value[1] <= value[3]:
            fallen_snowflake_list.append(key)
    return fallen_snowflake_list


def delete_snowflake():
    global snowflakes
    global fallen_snowflake_list
    for element in fallen_snowflake_list:
        snowflakes.__delitem__(element)

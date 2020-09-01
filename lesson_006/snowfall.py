# -*- coding: utf-8 -*-
import simple_draw as sd

fallen_snowflake_list = []
fallen_snowflake_count = 0


def create_snowflakes(n):
    snowflake_count = 0
    i = 0
    while snowflake_count < n:
        if globals().get('snowflake_' + str(i)):
            i += 1
        else:
            snowflake_name = 'snowflake_' + str(i)
            globals()[snowflake_name] = [sd.random_number(5, 200),
                                         sd.random_number(550, 650),
                                         sd.random_number(10, 70),
                                         sd.random_number(10, 20)]
            snowflake_count += 1


def drawing_snowflakes(color):
    for i in range(0, len(globals())):
        if globals().get('snowflake_' + str(i)):
            point = sd.get_point(globals().get('snowflake_' + str(i))[0], globals().get('snowflake_' + str(i))[1])
            sd.snowflake(point, globals().get('snowflake_' + str(i))[2], color)
        else:
            break


def moving_snowflakes():
    for i in range(0, len(globals())):
        if globals().get('snowflake_' + str(i)):
            globals().get('snowflake_' + str(i))[1] -= globals().get('snowflake_' + str(i))[3]
            globals().get('snowflake_' + str(i))[0] += sd.random_number(-5, 5)
        else:
            break


def fallen_snowflakes():
    global fallen_snowflake_list
    for i in range(0, len(globals())):
        if globals().get('snowflake_' + str(i)):
            if globals().get('snowflake_' + str(i))[1] <= globals().get('snowflake_' + str(i))[3]:
                fallen_snowflake_list.append(i)
        else:
            pass
    return fallen_snowflake_list


def delete_snowflake():
    global fallen_snowflake_list
    global fallen_snowflake_count
    fallen_snowflake_count = len(fallen_snowflake_list)
    for element in fallen_snowflake_list:
        globals().__delitem__('snowflake_' + str(element))
    fallen_snowflake_list.clear()

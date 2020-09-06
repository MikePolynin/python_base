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


# TODO, Немного смущает схема образования индекса 'snowflake_' + str(i).
#  Возможно с items можно будет уйти от неё. Она очень сильно растягивает код и по сути нужна
#  только при создании снежинки. А далее, мы можем просто идти по ключам словаря и работать с ними.

def drawing_snowflakes(color):
    global snowflakes
    # TODO, если идём в цикле по словарю, то правильней идти с items()
    #  Условный оператор if/else лишний.
    for i in range(0, len(snowflakes)):

        if snowflakes.get('snowflake_' + str(i)):
            point = sd.get_point(snowflakes.get('snowflake_' + str(i))[0], snowflakes.get('snowflake_' + str(i))[1])
            sd.snowflake(point, snowflakes.get('snowflake_' + str(i))[2], color)
        else:
            break


def moving_snowflakes():
    global snowflakes
    # TODO, если идём в цикле по словарю, то правильней идти с items()
    #  Условный оператор if/else лишний.
    for i in range(0, len(snowflakes)):
        print(i)
        if snowflakes.get('snowflake_' + str(i)):
            snowflakes.get('snowflake_' + str(i))[1] -= snowflakes.get('snowflake_' + str(i))[3]
            snowflakes.get('snowflake_' + str(i))[0] += sd.random_number(-5, 5)
        else:
            break


def fallen_snowflakes():
    global snowflakes
    global fallen_snowflake_list
    # TODO, если идём в цикле по словарю, то правильней идти с items()
    for i in range(0, len(snowflakes)):
        if snowflakes.get('snowflake_' + str(i)):
            if snowflakes.get('snowflake_' + str(i))[1] <= snowflakes.get('snowflake_' + str(i))[3]:
                fallen_snowflake_list.append(i)
        else:
            pass
    return fallen_snowflake_list


def delete_snowflake():
    global snowflakes
    global fallen_snowflake_list
    for element in fallen_snowflake_list:
        snowflakes.__delitem__('snowflake_' + str(element))

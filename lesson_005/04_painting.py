# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
import simple_draw
from python_base.lesson_005.drawing.rainbow import draw_rainbow
from python_base.lesson_005.drawing.wall import draw_house
from python_base.lesson_005.drawing.tree import draw_branches
from python_base.lesson_005.drawing.sun import draw_sun
from python_base.lesson_005.drawing.smile import smiles_draw
from python_base.lesson_005.drawing.snowfall import snowfall

simple_draw.resolution = (1500, 600)

draw_branches(simple_draw.get_point(1000, 30))
draw_house()

while True:
    simple_draw.start_drawing()
    snowfall()
    draw_sun(400, 500)
    smiles_draw(578, 181, simple_draw.random_color())
    draw_rainbow()
    simple_draw.finish_drawing()
    simple_draw.sleep(0.2)
    if simple_draw.user_want_exit():
        break

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

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
import lesson_005.drawing.rainbow
import lesson_005.drawing.wall
import lesson_005.drawing.tree


def smile(x, y, color):
    from lesson_005.drawing.smile import smiles_draw
    smiles_draw(x, y, color)


def sun(x, y):
    while True:
        center = simple_draw.get_point(x, y)
        simple_draw.circle(center, 40, simple_draw.COLOR_YELLOW, 0)
        angle = 0
        for line in range(1, 9):
            vector = simple_draw.get_vector(center, angle, 90, 5)
            vector.draw()
            angle = 45 * line
            simple_draw.sleep(0.1)
        import lesson_005.drawing.snowfall
        if simple_draw.user_want_exit():
            break


smile(578, 181, simple_draw.random_color())
sun(400, 500)

simple_draw.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

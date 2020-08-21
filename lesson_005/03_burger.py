# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

from lesson_005.my_burger import add_bread, add_cutlet, add_cucumber, add_tomato, add_mayonnaise, add_cheese, \
    add_mustard, add_ketchup, add_onion


def make_double_cheeseburger():
    print('Готовим двойной чизбургер:')
    add_bread()
    add_cutlet()
    add_cheese()
    add_cutlet()
    add_cheese()
    add_cucumber()
    add_mustard()
    add_ketchup()
    add_onion()
    add_bread()
    print('Двойной чизбургер готов')


def make_burger():
    print('Готовим гамбургер:')
    add_bread()
    add_cutlet()
    add_mustard()
    add_ketchup()
    add_onion()
    add_bread()
    print('Гамбургер готов')


make_double_cheeseburger()
make_burger()

# зачёт!

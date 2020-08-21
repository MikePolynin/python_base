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

from lesson_005.my_burger import bread, cutlet, cucumber, tomato, mayonnaise, cheese, mustard, ketchup, onion


def double_cheeseburger():
    print('Готовим двойной чизбургер:')
    bread()
    cutlet()
    cheese()
    cutlet()
    cheese()
    cucumber()
    mustard()
    ketchup()
    onion()
    bread()
    print('Двойной чизбургер готов')


def burger():
    print('Готовим гамбургер:')
    bread()
    cutlet()
    mustard()
    ketchup()
    onion()
    bread()
    print('Гамбургер готов')


double_cheeseburger()
burger()

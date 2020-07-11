#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)
print(zoo)

# уберите слона
#  и выведите список на консоль
# TODO, Михаил, всё правильно, вы верно уловили суть.
# TODO, это задание на поиск и использование списковых методов. "del" - интересный вариант,
#  который в итоге привёл в нужному результату, Но давайте попробуйем найти списковый метод для текущего задания.
#  Мы советуем первоначально обращаться к официальной документации python
#  https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20index. Пожалуйста ознакомьтесь,
#  возможно один из методов поможет нам в решении поставленной задачи.
del zoo[3]
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
lion_number = zoo.index('lion') + 1
lark_number = zoo.index('lark') + 1
print('Lion cage - ' + str(lion_number))
print('Lark cage - ' + str(lark_number))

# TODO, Михаил, суть Вы правильно поняли,
#  давайте попробуем для примере не приводить переменные в print к str, а "+" поменять на ",".

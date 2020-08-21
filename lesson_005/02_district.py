# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from lesson_005.district.central_street.house1 import room1 as folks_1, room2 as folks_2
from lesson_005.district.central_street.house2 import room1 as folks_3, room2 as folks_4
from lesson_005.district.soviet_street.house1 import room1 as folks_5, room2 as folks_6
from lesson_005.district.soviet_street.house2 import room1 as folks_7, room2 as folks_8

delimiter = ', '
all_folks = []
for folk in folks_1, folks_2, folks_3, folks_4, folks_5, folks_6, folks_7, folks_8:
    for tenant in folk.folks:
        all_folks.append(tenant)
print('На районе живут:', delimiter.join(all_folks))

# зачёт!

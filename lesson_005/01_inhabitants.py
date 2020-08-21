# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from lesson_005 import room_1 as folks_1
from lesson_005 import room_2 as folks_2

delimiter = ', '
for folk in folks_1, folks_2:
    all_folks = []
    for tenant in folk.folks:
        all_folks.append(tenant)
    print('В комнате', folk.__name__[-6:], 'живут:', delimiter.join(all_folks))

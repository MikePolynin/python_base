# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...
import room_1 as folks_1
import room_2 as folks_2

delimiter = ', '
for folks in folks_1, folks_2:
    print('В комнате', folks.__name__, 'живут:', delimiter.join(folks.folks))
# зачёт!

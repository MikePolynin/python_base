from random import randint

hidden_number = set()


def guess_the_number():
    global hidden_number
    # TODO, подсчёт количества попыток можно сделать глобальной переменной тоже и обнулять в этой функции.
    hidden_number.clear()
    hidden_number.add(randint(1, 9))
    while len(hidden_number) < 4:
        next_digit = randint(0, 9)
        hidden_number.add(next_digit)

    print(hidden_number)  # я пока что воспользуюсь этим print =)


def check_the_number(user_input):
    # TODO, а в этой функции можно вести подсчёт количества шагов. Добавляя +1 с каждой проверкой.
    result = {'bulls': 0, 'cows': 0}
    for user_digit_index, user_digit in enumerate(user_input):
        if user_digit in hidden_number:
            # TODO, получилась очень длинная строка.
            #  Можем просто проверять соответствует ли user_digit соответствующему числу hidden_number,
            #  которое найдём срезом по уще умеющемуся индексу user_digit_index.
            #  Только первоначально, необходимо будет создать переменную список из check_the_number =)
            if user_digit_index == list(hidden_number).index(user_digit):
                result['bulls'] += 1
            else:
                result['cows'] += 1
    return result

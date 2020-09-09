from random import randint

hidden_number = []


def guess_the_number():
    global hidden_number
    hidden_number.clear()
    first_digit = randint(1, 9)
    hidden_number.append(first_digit)
    # TODO, в этом месте можно обойтись без переменной first_digit. Сразу добавлять randint()
    # TODO, сейчас hidden_number это список, если сделать множеством (set), нам так же будут доступны срезы.
    #  И не надо будет проверять наличие рандомного числа в hidden_number.
    #  Если в set добавить уже имеющееся число, оно просто не добавится.
    while len(hidden_number) < 4:
        next_digit = randint(0, 9)
        if next_digit not in hidden_number:
            hidden_number.append(next_digit)


def check_the_number(user_input):
    result = {'bulls': 0, 'cows': 0}
    # TODO, в этом месте по user_input лучше идти с enumerate, в таком случае,
    #  нам будет доступен индекс числа и его не нужно будет вычислять методом index()
    for user_digit in user_input:
        if user_digit in hidden_number:
            if user_input.index(user_digit) == hidden_number.index(user_digit):
                result['bulls'] += 1
            else:
                result['cows'] += 1
    return result


guess_the_number()  # TODO, лишний вызов функции.

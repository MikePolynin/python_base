from random import randint

hidden_number = set()


def guess_the_number():
    global hidden_number
    hidden_number.clear()
    hidden_number.add(randint(1, 9))
    while len(hidden_number) < 4:
        next_digit = randint(0, 9)
        hidden_number.add(next_digit)


def check_the_number(user_input):
    result = {'bulls': 0, 'cows': 0}
    for user_digit_index, user_digit in enumerate(user_input):
        if user_digit in hidden_number:
            if user_digit_index == list(hidden_number).index(user_digit):
                result['bulls'] += 1
            else:
                result['cows'] += 1
    print(hidden_number)
    return result

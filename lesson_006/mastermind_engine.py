from random import randint

# hidden_number = set()  # variant 1
hidden_number = []  # variant 2
steps = 0


def guess_the_number():
    global hidden_number
    global steps
    steps = 0
    hidden_number.clear()

    # variant 1
    # hidden_number.add(randint(1, 9))
    # while len(hidden_number) < 4:
    #     next_digit = randint(0, 9)
    #     hidden_number.add(next_digit)

    # variant 2
    hidden_number.append(randint(1, 9))
    while len(hidden_number) < 4:
        next_digit = randint(0, 9)
        if next_digit not in hidden_number:
            hidden_number.append(next_digit)

    # print(hidden_number)


def input_check():
    while True:
        user_input = input('Input your number:')
        if len(user_input) != 4:
            print('Wrong input')
        elif user_input[0] == '0':
            print('Wrong input')
        elif not user_input.isdigit():
            print('Wrong input')
        elif len(set(user_input)) != 4:
            print('Wrong input')
        else:
            user_input_list = [int(element) for element in user_input]
            return user_input_list


def check_the_number(user_input):
    global steps
    steps += 1
    result = {'bulls': 0, 'cows': 0}
    for user_digit_index, user_digit in enumerate(user_input):
        if user_digit in hidden_number:
            if user_digit == list(hidden_number)[user_digit_index]:
                result['bulls'] += 1
            else:
                result['cows'] += 1
    return result

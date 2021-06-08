DATA_LEN = 4


def get_data():
    """
    :return: корректный input
    """
    print('Введите через пробел 4 числа и нажмите enter: ')
    res, check_res = read_data(input())

    while not check_res['status']:

        print(check_res['msg'])
        res, check_res = read_data(input())

    return res


def read_data(input_data):
    """
    читает вход и проверяет на корректность
    :return:
    - результат,
    - словарь со статусом проверки корректности
                        и сообщением при некорректном вводе
    """
    split_data = [data for data in input_data.split() if data != '']

    check_res = check_data(split_data)

    if check_res['status']:
        res = [float(data) for data in split_data]
    else:
        res = False

    return res, check_res


def check_data(split_data):
    """
    :param split_data: разделенные через пробле данные, без пустых строк
    :return: словарь со статусом проверки корректности и сообщением
    """
    res = {'status': 1,
           'msg': 'correct input'}

    if not len(split_data) == DATA_LEN:
        res['status'] = 0
        res['msg'] = 'Введите 4 числа'
        return res

    for string in split_data:
        if not is_digit(string):
            res['status'] = 0

            if string.replace(',', '', 1).isdigit():
                res['msg'] = 'Вещественные числа должны быть разделены точкой'
            else:
                res['msg'] = 'Введите только числа'
            return res

    return res


def is_digit(data):
    """
    :param data: строка
    :return: bool - является ли data числом
    """
    if data[0] == '-':
        return data[1:].replace('.', '', 1).isdigit()

    return data.replace('.', '', 1).isdigit()


def calculate(data):
    """
    :param data: список с 4 вещественными числами
    :return: словарь со статусом вычислений и результатом
    """
    a, b, c, d = data

    res = {'status': 1,
           'res': -1}

    if c + d == 0:
        print('Деление на 0')
        res['status'] = 0
    else:
        res['res'] = (a + b)/(c + d)

    return res


def main_func(print_res=True):
    data = get_data()
    res = calculate(data)

    while not res['status']:
        data = get_data()
        res = calculate(data)

    if print_res:
        print('a, b, c, d = ', *data)
        print('(a + b)/(c+d) = ', res['res'])

    return data, res['res']


if __name__ == '__main__':
    main_func()

"""Задача №1.
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц,
за которыми следует какое-то количество подряд идущих нулей:
111111111111111111111111100000000.
"""

tests = [
    ['test1', '0', None],
    ['test2', '1', None],
    ['test3', '', None],
    ['test4', '10', 1],
    ['test6', '11110', 4],
    ['test7', '11111000000', 5],
    ['test8', '1000000', 1],
    ['test9', '111111111111111111111111100000000', 25],
    ['test10', '111111111110000000000000000', 11]
]


def task(array):
    # В условии указана работа со списком, а в примере
    # на вход функции подаётся строка. Работаем со строками,
    # если подаётся массив, преобразовываем его
    if type(array) == list:
        array = ''.join(map(str, array))

    if len(array) < 2 or array[-1] != '0' or array[0] != '1':
        return None

    def search(array, x=0):
        l = int(len(array) / 2)

        if array[l] == '0':
            if len(array) == 1:
                return x
            else:
                return (search(array[:l], x=x))
        else:
            if len(array) == 1:
                x += 1
                return x
            else:
                return (search(array[l:], x=x + l))

    x = search(array)

    return x


if __name__ == '__main__':
    for test in tests:
        answer = task(test[1])
        result = 'Success' if answer == test[2] else 'Failure'
        if result == 'Success':
            print('{} - {}'.format(test[0], result))
        else:
            print('{} - {}\nExpected: {}, Answer: {}'.format(test[0], result,
                                                             test[2], answer))

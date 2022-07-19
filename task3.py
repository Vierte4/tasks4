'''Когда пользователь заходит на страницу урока, мы сохраняем время его захода.
Когда пользователь выходит с урока (или закрывает вкладку, браузер –
в общем как-то разрывает соединение с сервером), мы фиксируем время выхода
с урока. Время присутствия каждого пользователя на уроке хранится у нас в виде
интервалов. В функцию передается словарь, содержащий три списка с таймстемпами
(время в секундах):'''

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                        1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                        1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009,
                        1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480,
                        1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
                        1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]


def fix_intervals(interval):
    # Сортирует начала и концы интервалов и соединяет все пересекающиеся интервалы в один

    start = [a for a in interval[::2]]
    end = [a for a in interval[1::2]]
    start.sort()
    end.sort()
    result = []

    a = 0
    while a < len(start):
        c = 0

        while a + c < len(start) - 1 and start[a + c + 1] < end[a + c]:
            c += 1
        result.append(start[a])
        result.append(end[a + c])

        a += c + 1

    return result


def appearance(intervals):
    time = 0
    b = 0
    tutor = fix_intervals(intervals['tutor'])
    pupil = fix_intervals(intervals['pupil'])
    lesson = intervals['lesson']
    l_pupil = len(pupil)
    l_tutor = len(tutor)
    for a in range(0, l_pupil, 2):
        while b < l_tutor:
            if pupil[a] > tutor[b + 1]:
                b += 2
                continue
            delta = max(
                min(pupil[a + 1], tutor[b + 1], lesson[1]) - max(pupil[a],
                                                                 tutor[b],
                                                                 lesson[0]), 0)
            time += delta
            if pupil[a + 1] < tutor[b + 1] and a != l_pupil:
                break
            b += 2
    return time


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test[
            'answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

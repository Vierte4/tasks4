"""В нашей школе мы не можем разглашать персональные данные пользователей,
но чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они
имеют в виду (у преподавателей, например, часто учится несколько Саш),
мы генерируем пользователям уникальные и легко произносимые имена. Имя у нас
состоит из прилагательного, имени животного и двузначной цифры. В итоге
получается, например, "Перламутровый лосось 77". Для генерации таких имен мы
и решали следующую задачу:
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR)
и вывести количество животных на каждую букву алфавита. Результат должен
 получиться в следующем виде:
А: 642
Б: 412
В:....
"""

import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'


def counter(url):
    book = {'А': 0}
    key = 'А'
    while True:
        response = requests.get(url).text
        page = BeautifulSoup(response, 'html')
        words = page.find(attrs={'class': 'mw-category mw-category-columns'})
        next_page = page.find('a', string='Следующая страница')
        if not next_page:
            return book
        url = 'https://ru.wikipedia.org' + next_page.get('href')

        words = words.text.split('\n')[1:]
        for word in words:
            if key != word[0]:
                # Ограничение русским алфавитом
                # if word[0] == ['A']:
                #    return book
                key = word[0]
                if not book.get(word[0]):
                    book[key] = 0
            book[key] += 1



if __name__ == '__main__':
    print(counter(url=url))

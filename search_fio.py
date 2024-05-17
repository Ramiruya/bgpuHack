import json
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
import google_parse

def select_fio(json_path):
    # Загрузка JSON данных
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Извлечение всех ФИО в список
    fio_list = []
    for faculty in data.values():
        for department in faculty.values():
            for user in department:
                fio_list.append(user['fio'])

    # Создание автодополнения для ФИО
    fio_completer = WordCompleter(fio_list, ignore_case=True)

    # Создание сессии для интерактивного ввода
    session = PromptSession(completer=fio_completer, auto_suggest=AutoSuggestFromHistory())

    while True:
        try:
            user_input = session.prompt(u'Введите ФИО: ')
        except KeyboardInterrupt:
            break
        except EOFError:
            break
        else:
            print(f'Выбранное ФИО: {user_input}')
            google_parse.scholar_search(user_input,json_path)
            return

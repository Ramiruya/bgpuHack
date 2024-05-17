import json
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
import google_parse

def select_states(json_path):
    # Загрузка JSON данных
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Извлечение всех ФИО в список
    states_list = []
    for faculty in data.values():
        for department in faculty.values():
            for user in department:
                try:
                    for state in user['states']:
                        states_list.append(state['state'])
                except KeyError:
                    pass

    # Создание автодополнения для ФИО
    states_completer = WordCompleter(states_list, ignore_case=True)

    # Создание сессии для интерактивного ввода
    session = PromptSession(completer=states_completer, auto_suggest=AutoSuggestFromHistory())

    while True:
        try:
            user_input = session.prompt(u'Введите название статьи: ')
        except KeyboardInterrupt:
            break
        except EOFError:
            break
        else:
            print(f'Выбранная статья: {user_input}')
            for faculty in data.values():
                for department in faculty.values():
                    for member in department:
                        if 'states' in member:
                            for state in member['states']:
                                if state['state'] == user_input:
                                    print(f"Post: {member.get('post')}")
                                    print(f"FIO: {member.get('fio')}")
                                    print(f"User Link: {member.get('user_link')}")
                                    print("---")
                                    print(f"State: {state.get('state')}")
                                    print(f"URL: {state.get('url')}")
                                    print('\n\n\n')
            # google_parse.scholar_search(user_input,json_path)
            return
